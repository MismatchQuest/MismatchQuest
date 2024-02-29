from prompters.BaseCongenFeedbackPrompt import BaseCongenFeedbackPrompt
from prompts.coco_prompts import TYPE_TO_FEW_SHOT_PROMPT

class CocoPrompt(BaseCongenFeedbackPrompt):
    def __init__(self, args):
        super().__init__(args)
        self.type_to_few_shot_prompt = TYPE_TO_FEW_SHOT_PROMPT

    def get_caption(self, row):
        return max(eval(row['captions']), key=len)  # Take the longest caption

