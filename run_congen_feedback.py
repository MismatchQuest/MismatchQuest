import argparse

from prompters.CocoPrompt import CocoPrompt
from prompters.Flickr30kPrompt import Flickr30kPrompt
from prompters.ImageRewardPrompt import ImageRewardPrompt
from prompters.LocalizedNarrativesPrompt import LocalizedNarrativesPrompt
from prompters.PickaPicPrompt import PickaPicPrompt

COCO_CSV_PATH = None
PICKAPIC_CSV_PATH = None 
IMAGE_REWARD_CSV_PATH = None 
LOCALIZED_NARRATIVES_CSV_PATH = None
FLICKR30K_CSV_PATH = None 
ADE20K_CSV_PATH = None

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='coco')
    parser.add_argument('--input_csv', type=str, default=COCO_CSV_PATH)

    parser.add_argument('--output_dir', type=str,
                        default=None)
    parser.add_argument('--range', type=str, default=None)
    parser.add_argument('--save_every_n', type=int, default=100)

    args = parser.parse_args()

    print("*** ARGS ***")
    print(args)

    return args


def main(args):
    if args.dataset == 'coco':
        prompter = CocoPrompt(args)
    elif args.dataset == 'pickapic':
        prompter = PickaPicPrompt(args)
    elif args.dataset == 'imagereward':
        prompter = ImageRewardPrompt(args)
    elif args.dataset == 'flickr30k':
        prompter = Flickr30kPrompt(args)
    elif args.dataset in ['ade20k', 'open_images']:
        prompter = LocalizedNarrativesPrompt(args)
    else:
        raise Error('Dataset not supported')

    congen_df = prompter.run_congen()
    prompter.save_df(congen_df)


if __name__ == '__main__':
    args = parse_args()
    main(args)
