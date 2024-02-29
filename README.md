# Mismatch Quest: Visual and Textual Feedback for Image-Text Misalignment
![alt text](https://github.com/MismatchQuest/MismatchQuest/blob/main/imgs/teaser.jpg?raw=True)
___
This repository contains the code and instructions to reproduce the results of the paper "Mismatch Quest: Visual and Textual Feedback for Image-Text Misalignment".

## Getting Started

First, clone the repository and install the required dependencies:

```bash
git clone https://github.com/MismatchQuest/MismatchQuest
pip install -r requirements.txt
```

## Textual-Visual Feedback Generation (Training data)
In order to reproduce our generation pipeline, we offer the following instructions:

### Set your Google Cloud credentials
At `consts.py` file you need to set the values for the constants:

`GOOGLE_PROJECT_NAME` - The name of your project at Google Cloud
`GOOGLE_APPLICATION_CREDENTIALS_PATH` - Absolute path to your credentials.json file. For more instructions how to get a `.json` credentials file: [link](https://developers.google.com/workspace/guides/create-credentials)

### Run the generation script
```
python run_congen_feedback.py --dataset <DATASET> --input_csv <INPUT_CSV_PATH> --output_dir <OUTPUT_DIR_PATH>
```
Arguments:
- `--dataset` - Dataset name to generate from: `['coco', 'pickapic', 'imagereward', 'flickr30k', 'ade20k', 'open_images']`
- `--input_csv` - Path for the input .csv file according to the dataset.
- `--output_dir` - Output directory path to save the generated file.
- [Optional] `--range` - You can split the .csv file by range using this argument as follows: `LOW_RANGE,HIGH_RANGE` for example: `--range 100,200`
- [Optional] `--save_every_n` - Argument that marks saving frequency during generation.

Note: As explained in the paper, the image descriptions of ADE20K and OpenImages datasets (taken from LocalizedNarratives dataset) where pre-processed using another script in order to summarize the long description into a short caption.
Before generating `Textual-Visual Feedback` for the mentioned datasets you need to run the following script:
```
python LocalizedNarrativesDescToCaption.py --input_jsonl_path <INPUT_JSONL_PATH> --output_dir <OUTPUT_DIR_PATH>
```
Arguments:
- `--input_jsonl_path` - Path for the input .jsonl downloaded from [LocalizedNarratives](https://google.github.io/localized-narratives/)
- `--output_dir` - Output directory path to save the generated file.
- [Optional] `--range` - You can split the .csv file by range using this argument as follows: `LOW_RANGE,HIGH_RANGE` for example: `--range 100,200`
- [Optional] `--save_every_n` - Argument that marks saving frequency during generation.


# SEETrue-Feedback dataset
SEETrue-Feedback a comprehensive alignment benchmark. It features 2,008 human-annotated instances that highlight textual and visual feedback.
You can download the dataset at the following [link](https://github.com/MismatchQuest/MismatchQuest/blob/main/SeeTRUE_Feedback.csv)

