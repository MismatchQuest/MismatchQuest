from prompters.BaseCongenFeedbackPrompt import BaseCongenFeedbackPrompt
from prompts.imagereward_prompt import TYPE_TO_FEW_SHOT_PROMPT

class ImageRewardPrompt(BaseCongenFeedbackPrompt):
    def __init__(self, *args):
        super().__init__(*args)
        self.type_to_few_shot_prompt = TYPE_TO_FEW_SHOT_PROMPT

    def get_caption(self, row):
        return eval(row['finetuned_captions'])[0]  # Return first result, it's the one with the highest score
