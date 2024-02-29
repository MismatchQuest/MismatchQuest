from prompters.BaseCongenFeedbackPrompt import BaseCongenFeedbackPrompt
from prompts.localized_narratives_prompt import TYPE_TO_FEW_SHOT_PROMPT


class LocalizedNarrativesPrompt(BaseCongenFeedbackPrompt):
    def __init__(self, args):
        super().__init__(args)
        self.type_to_few_shot_prompt = TYPE_TO_FEW_SHOT_PROMPT

    def get_caption(self, row):
        return row['chat-bison_caption']
