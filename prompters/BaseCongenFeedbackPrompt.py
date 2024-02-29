import os
import time
import pandas as pd
import numpy as np
from tqdm import tqdm
import openai
import spacy
from tenacity import retry, stop_after_attempt, wait_random_exponential, wait_exponential
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from pos_tagging_spacy import identify_augmentation_type_with_random_proposal
import re
from call_palm_with_backoff import call_palm_with_backoff

import consts

# Cloud settings
aiplatform.init(project=consts.GOOGLE_PROJECT_NAME)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = consts.GOOGLE_APPLICATION_CREDENTIALS_PATH

DEBUG = False

BASE_CONGEN_PROMPT_V3_MERGED_MISALIGNMENT = """Your primary task is to generate subtly contradictory captions based on an original input caption. This test is intended to observe the capacity of models to recognize nuanced semantic changes which might be easily detected by humans but challenging for models.

Guidelines:
Caption Modification: Introduce a delicate semantic change to the original caption. The alteration should subtly change the meaning while remaining potentially overlooked. It should neither be drastic nor too minor.
MISALIGNMENT: After constructing your contradictory caption, articulate the disparity between the original CAPTION and the CONTRADICTION in a crisp manner. The elucidation should:
Spotlight the deviation from the angle of the CONTRADICTION, pinpointing what the CONTRADICTION suggests but is countered by the CAPTION.
For the CAPTION description, ensure it thoroughly represents the true content of the CAPTION (e.g., "CAPTION: a blue ball on a shelf").
For the CONTRADICTION description, keep it brief and directly replicate the relevant segment (e.g., "CONTRADICTION: green ball").
MISALIGNMENT TYPE: Categorize the nature of the misalignment into one of the following categories: Object/Noun, Attribute/Adjective, Action/Verb, or Relation
"""


class BaseCongenFeedbackPrompt:
    def __init__(self, args):
        self.args = args
        self.df = pd.read_csv(args.input_csv)
        self.output_dir = args.output_dir
        self.context_prompt = """Your primary task is to generate subtly contradictory captions based on an original input caption. This test is intended to observe the capacity of models to recognize nuanced semantic changes which might be easily detected by humans but challenging for models.

        Guidelines:
        Caption Modification: Introduce a delicate semantic change to the original caption. The alteration should subtly change the meaning while remaining potentially overlooked. It should neither be drastic nor too minor.
        MISALIGNMENT: After constructing your contradictory caption, articulate the disparity between the original CAPTION and the CONTRADICTION in a crisp manner. The elucidation should:
        Spotlight the deviation from the angle of the CONTRADICTION, pinpointing what the CONTRADICTION suggests but is countered by the CAPTION.
        For the CAPTION description, ensure it thoroughly represents the true content of the CAPTION (e.g., "CAPTION: a blue ball on a shelf").
        For the CONTRADICTION description, keep it brief and directly replicate the relevant segment (e.g., "CONTRADICTION: green ball").
        MISALIGNMENT TYPE: Categorize the nature of the misalignment into one of the following categories: Object/Noun, Attribute/Adjective, Action/Verb, or Relation
        """
        self.model = ChatModel.from_pretrained("chat-bison@001")
        self.nlp = spacy.load("en_core_web_sm")
        self.augmentation_counts = {
            "Relation": 0,
            "Action/Verb": 0,
            "Attribute/Adjective": 0,
            "Object/Noun": 0
        }
        timestr = time.strftime("%Y%m%d-%H%M%S")
        output_filename = f"{os.path.split(args.input_csv)[1].replace('.csv', '')}_{timestr}_congen.csv"

        if DEBUG:
            sampled_idxs = np.random.randint(low=0, high=len(self.df), size=100)
            self.df = self.df.iloc[sampled_idxs]
            output_filename = output_filename.replace(".csv", "_DEBUG.csv")

        if args.range is not None:
            low_range, high_range = args.range.split(",")
            low_range, high_range = int(low_range), int(high_range)
            print(f'Slicing df to range: {low_range} - {high_range}')
            self.df = self.df if DEBUG else self.df[low_range:high_range]
            output_filename = output_filename.replace(".csv", f"_range_{low_range}-{high_range}.csv")

        self.output_csv = os.path.join(self.output_dir, output_filename)
        os.makedirs(self.output_dir, exist_ok=True)
        self.max_count_per_type = int(len(self.df) / 4)
        self.save_every_n = args.save_every_n
        self.type_to_few_shot_prompt = NotImplemented

    def run_congen(self):
        df = self.df
        new_rows = []
        for i, (df_idx, row) in tqdm(enumerate(df.iterrows()), total=len(df)):
            caption = self.get_caption(row)
            augmentation_type, proposal = self.get_type_proposal(caption)
            sample = self.prepare_sample(caption, augmentation_type, proposal)
            instructions_and_type = f"{BASE_CONGEN_PROMPT_V3_MERGED_MISALIGNMENT}{self.type_to_few_shot_prompt[augmentation_type]}"
            ## Trigger LLM
            chat = self.model.start_chat(context=instructions_and_type)
            output = call_palm_with_backoff(chat, sample, mode='chat')
            reply = output.text
            reply = reply.replace("[", "").replace("]", "")
            reply_processed = self.split_reply_v2(reply)

            row['feedback'] = reply_processed['feedback']
            row['feedback_clean'] = reply_processed['feedback_clean']
            row['caption_misalignment'] = reply_processed['contradiction_bbox']
            row['visual_misalignment'] = reply_processed['contradiction_bbox']
            row['negative_caption'] = reply_processed['contradiction']
            row['misalignment_type'] = reply_processed['contradiction_type']
            row['positive_caption'] = caption

            new_rows.append(row.to_dict())
            if i % self.save_every_n == 0:  ## Save current results
                print(f'Saving at: {self.output_csv}')
                pd.DataFrame(new_rows).to_csv(self.output_csv)

        print(f'Saving at: {self.output_csv}')
        pd.DataFrame(new_rows).to_csv(self.output_csv)
        return pd.DataFrame(new_rows)

    def save_df(self, df):
        df.to_csv(self.output_csv)

    def prepare_sample(self, caption, augmentation_type, proposal):
        sample = self.context_prompt.replace('<context_captions>', caption)
        if augmentation_type == "Relation":
            sample = sample.replace('<misalignment_type>',
                                    f"{augmentation_type} , You can use the following suggestion: {proposal}.")
        elif augmentation_type == "Action/Verb":
            sample = sample.replace('<misalignment_type>', f"{augmentation_type}.")
        elif augmentation_type == "Attribute/Adjective":
            sample = sample.replace('<misalignment_type>', f"{augmentation_type}")
        elif augmentation_type == "Object/Noun":
            sample = sample.replace('<misalignment_type>', augmentation_type)
        else:  # No specific request for misalignment type, remove the sentence from sample!
            sample = sample.replace('Create a MISALIGNMENT of type: <misalignment_type>', '')
        return sample

    def get_type_proposal(self, caption):
        caption_pos_tags = [(token.text, token.pos_) for token in self.nlp(caption)]
        augmentation_type, proposal = identify_augmentation_type_with_random_proposal(caption_pos_tags,
                                                                                      self.augmentation_counts,
                                                                                      self.max_count_per_type)
        return augmentation_type, proposal

    def get_caption(self, caption):
        raise NotImplementedError()

    @staticmethod
    def split_reply_v2(reply):
        result = {
            'contradiction': '', 'feedback_clean': '', 'feedback': '', 'caption_bbox': '',
            'contradiction_bbox': '', 'contradiction_type': ''}
        reply_lines = reply.splitlines()

        for line in reply_lines:
            line = line.strip()
            if line.startswith('CONTRADICTION:'):
                result['contradiction'] = line.strip().replace('CONTRADICTION:', '').strip()
            elif line.startswith('MISALIGNMENT:'):
                result['feedback'] = line.strip().replace('MISALIGNMENT:', '').strip()
            elif line.startswith('MISALIGNMENT TYPE:'):
                result['contradiction_type'] = line.strip().replace('MISALIGNMENT TYPE:', '').strip()

        if result['feedback']:
            feedback_clean, caption_bbox, contradiction_bbox = BaseCongenFeedbackPrompt.extract_parenthesis_content(
                result['feedback'])
            result['feedback_clean'] = feedback_clean
            result['contradiction_bbox'] = contradiction_bbox
            result['caption_bbox'] = caption_bbox

        return result

    @staticmethod
    def extract_parenthesis_content(s):
        caption = ''
        contradiction = ''
        caption_list = []
        contradiction_list = []
        without_parenthesis = ''
        # Extract all contents inside parenthesis
        inside_parenthesis = re.findall(r'\((.*?)\)', s)

        # # If there are more than 2 parentheses, raise an error
        # if len(inside_parenthesis) > 2:
        #     return without_parenthesis, caption, contradiction

        # Remove all contents inside parenthesis including the parenthesis
        without_parenthesis = re.sub(r'\s?\(.*?\)', '', s).strip()

        for content in inside_parenthesis:
            if "CAPTION:" in content:
                caption = content.replace("CAPTION:", "").strip()
                caption_list.append(caption)
            elif "CONTRADICTION:" in content:
                contradiction = content.replace("CONTRADICTION:", "").strip()
                contradiction_list.append(contradiction)

        if len(caption_list) > 0:
            caption = " . ".join(caption_list)
        if len(contradiction_list) > 0:
            contradiction = " . ".join(contradiction_list)
        return without_parenthesis, caption, contradiction
