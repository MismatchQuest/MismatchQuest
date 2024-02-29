from prompters.BaseCongenFeedbackPrompt import BaseCongenFeedbackPrompt
from prompts.pickapic_prompt import TYPE_TO_FEW_SHOT_PROMPT


class PickaPicPrompt(BaseCongenFeedbackPrompt):
    def __init__(self, *args):
        super().__init__(*args)
        self.type_to_few_shot_prompt = TYPE_TO_FEW_SHOT_PROMPT

    def get_caption(self, row):
        return eval(row['finetuned_captions_jpg'])[0]  # Return first result, its the one with highest score
