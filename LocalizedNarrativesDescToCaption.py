import argparse
import json
import time
import os
from tqdm import tqdm
import pandas as pd
from call_palm_with_backoff import call_palm_with_backoff
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel
import consts

# Cloud settings
aiplatform.init(project=consts.GOOGLE_PROJECT_NAME)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = consts.GOOGLE_APPLICATION_CREDENTIALS_PATH

INSTRUCTION_PROMPT = """Task Definition: Extracting Concise Image Captions

Input: 
DESCRIPTION: A long description of an image containing various objects, people, and scene details.

Output: 
CAPTION: A succinct and clear caption sentence that summarizes the most important features of the image, including primary objects, their spatial relationships, and key contextual elements.

Process:
1. Read the full description to understand the image content.
2. Identify main objects, people, and their relationships.
3. Choose primary objects and relevant spatial arrangements.
4. Exclude redundant instances of the same object.
5. Incorporate contextual details like the background.
6. Craft a clear, concise caption sentence.
7. Review for accuracy and coherence.
8. Edit to achieve an appropriate length.
9. Verify the caption's representation of the image.

The goal is to create a concise caption that effectively communicates the image's core elements and meaning.

Examples:
DESCRIPTION:  There is a table. There is a radio,plate,biscuits,cup,saucer and photo poster on a table. There is a sofa on the center. There is a table and stool on the right side. There is a bowl on a stool. We can see in the background white color wall and lamp. 
CAPTION: A radio is placed on a table. Beside the table there is a stool. The background is a white color woll.

DESCRIPTION:  There is a lady wearing watch and goggles is holding a dog and a bag. On the right side there few people, mesh fencing. And there is a person holding a video camera. On the left side there is a mesh fencing with poles. Near to that there are dogs. In the background there is a building and sky with clouds. 
CAPTION: A lady wearing watch and googles is holding a dog and a bag. There are people on her right side. There is a bulding and sky with clouds at the background
"""

SAMPLE = """DESCRIPTION: <description>
CAPTION: 
"""

OPEN_IMAGES_TRAIN_JSONL_PATH = "/home/dcor/datasets/Localized_Narratives/open_images_train_v6_captions.jsonl"
OPEN_IMAGES_VAL_JSONL_PATH = "/home/dcor/datasets/Localized_Narratives/open_images_validation_captions.jsonl"
OPEN_IMAGES_TEST_JSONL_PATH = "/home/dcor/datasets/Localized_Narratives/open_images_test_captions.jsonl"
ADE20K_TRAIN_JSONL_PATH = "/home/dcor/datasets/Localized_Narratives/ade20k_train_captions.jsonl"
ADE20K_VAL_JSONL_PATH = "/home/dcor/datasets/Localized_Narratives/ade20k_validation_captions.jsonl"


class LocalizedNarrativesDescToCaption:
    def __init__(self, args):
        self.args = args
        self.save_every_n = args.save_every_n

        with open(args.input_jsonl_path, 'r') as f:
            self.num_of_lines = sum(1 for line in f)

        self.jsonl_file = open(args.input_jsonl_path, 'r')
        self.model = ChatModel.from_pretrained("chat-bison@001")
        if args.range is not None:
            self.low_range, self.high_range = args.range.split(",")
            self.low_range, self.high_range = int(self.low_range), int(self.high_range)
            print(f'Slicing df to range: {self.low_range} - {self.high_range}')

        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.output_dir = args.output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.output_csv_path = os.path.join(self.output_dir,
                                            f"{os.path.basename(args.input_jsonl_path)}_{timestr}_captions.csv")

    def get_caption(self, row):
        return row['chat-bison_caption']

    def run_description_to_caption(self):
        pbar = tqdm(enumerate(self.jsonl_file), total=self.num_of_lines)
        new_rows = []
        for i, line in pbar:
            # Parse the JSON data from the line
            json_data = json.loads(line)

            chat = self.model.start_chat(context=INSTRUCTION_PROMPT)
            output = call_palm_with_backoff(chat, SAMPLE.replace('<description>', json_data['caption']), mode='chat')

            reply = output.text
            json_data['chat-bison_caption'] = reply
            new_rows.append(json_data)

            if i % self.save_every_n == 0:  ## Save current results
                print(f'Saving at: {self.output_csv_path}')
                df = pd.DataFrame(new_rows)
                df.to_csv(self.output_csv_path)

        df = pd.DataFrame(new_rows)
        return df

    def save_df(self, df):
        df.to_csv(self.output_csv)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_jsonl_path', type=str, default=OPEN_IMAGES_TRAIN_JSONL_PATH)
    parser.add_argument('--output_dir', type=str,
                        default=None)
    parser.add_argument('--range', type=str, default=None)
    parser.add_argument('--save_every_n', type=int, default=100)

    args = parser.parse_args()

    print("*** ARGS ***")
    print(args)

    return args


if __name__ == '__main__':
    args = parse_args()
    prompter = LocalizedNarrativesDescToCaption(args)
    df = prompter.run_description_to_caption()
    prompter.save_df(df)
