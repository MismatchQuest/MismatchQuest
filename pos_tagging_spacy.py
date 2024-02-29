# pip install spacy
# python -m spacy download en_core_web_sm
import random
import spacy
import json
import pandas as pd

pickapic_path = None 
nlp = spacy.load("en_core_web_sm")

def main():

    """ spacy example """
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)


    pickapic = pd.read_csv(pickapic_path, nrows=1000)
    pickapic['finetuned_captions_jpg_0'] = pickapic['finetuned_captions_jpg_0'].apply(json.loads)
    pickapic['first_caption_jpg0'] = pickapic['finetuned_captions_jpg_0'].apply(lambda x: x[0])
    captions_sample = list(pickapic['first_caption_jpg0'].head(100))

    # Augmentation distribution counters
    max_count = len(captions_sample) * 0.25
    augmentation_counts = {
        "Relation": 0,
        "Action/Verb": 0,
        "Attribute/Adjective": 0,
        "Object/Noun": 0
    }

    captions_annotated = []
    for cap in captions_sample:
        caption_pos_tags = [(token.text, token.pos_) for token in nlp(cap)]
        augmentation_type, proposal = identify_augmentation_type_with_random_proposal(caption_pos_tags, augmentation_counts, max_count)
        captions_annotated.append({'caption': cap, 'pos_tags': caption_pos_tags, 'augmentation_type': augmentation_type, 'proposal': proposal})

    augmentation_distribution = pd.DataFrame(captions_annotated).groupby('augmentation_type').size()
    print(augmentation_distribution)

    print("Done")


def identify_augmentation_type_with_random_proposal(sentence_annotated, augmentation_counts, max_count):
    priority_list = ["Relation", "Action/Verb", "Attribute/Adjective", "Object/Noun"]

    # Dictionary mapping spatial relations to their list of possible augmentations
    spatial_relations_map = {
        "above": ["below"],
        "adjacent to": ["far from", "opposite"],
        "alongside": ["opposite", "far from"],
        "amid": ["outside", "beside"],
        "amidst": ["outside", "beside"],
        "among": ["separate from", "outside"],
        "amongst": ["separate from", "outside"],
        "atop": ["beneath", "below"],
        "behind": ["in front of", "opposite"],
        "ahead": ["behind", "opposite"],
        "beneath": ["atop", "above"],
        "beside": ["apart from", "distant from"],
        "between": ["outside", "apart from"],
        "beyond": ["before", "behind"],
        "by": ["away from", "distant from"],
        "close to": ["distant from", "far from"],
        "facing": ["turning away from", "opposite"],
        "opposite": ["alongside", "beside"],
        "far from": ["adjacent to", "close to"],
        "in line with": ["perpendicular to", "opposite"],
        "inside": ["outside", "beyond"],
        "over": ["under", "beneath"],
        "parallel to": ["perpendicular to", "opposite"],
        "surrounding": ["enclosed by", "outside"],
        "toward": ["away from", "opposite"],
        "underneath": ["above", "atop"],
        "in front of": ["behind", "opposite"],
        "to the left": ["to the right", "opposite"],
        "to the right": ["to the left", "opposite"]
    }
    spatial_relations_map = {
    "above": ["below", "underneath"],
    "adjacent to": ["far from", "opposite", "distant from"],
    "alongside": ["opposite", "far from", "away from"],
    "amid": ["outside", "beside", "between"],
    "amidst": ["outside", "apart from"],
    "among": ["separate from", "outside", "apart from"],
    "amongst": ["isolated from", "distinct from"],
    "atop": ["beneath", "under", "below"],
    # "behind": ["in front of", "ahead", "opposite"],
    # "ahead": ["behind", "trailing", "opposite"],
    "beneath": ["atop", "above", "overhead"],
    # "beside": ["apart from", "distant from", "far from"],
    # "between": ["outside", "apart from", "flanking"],
    # "beyond": ["before", "behind", "within"],
    # "by": ["away from", "distant from", "beside"],
    "close to": ["distant from", "far from", "apart from"],
    "facing": ["turning away from", "opposite", "averting"],
    # "opposite": ["alongside", "beside", "parallel to"],
    "far from": ["adjacent to", "close to", "beside"],
    # "in line with": ["perpendicular to", "opposite", "diverging from"],
    "inside": ["outside", "beyond", "surrounding"],
    "over": ["under", "beneath", "below"],
    # "parallel to": ["perpendicular to", "opposite", "intersecting"],
    # "surrounding": ["enclosed by", "outside", "within"],
    "toward": ["away from", "retreating from", "opposite"],
    "underneath": ["above", "atop", "overhead"],
    # "in front of": ["behind", "opposite", "trailing"],
    "to the left": ["to the right", "opposite", "adjacent to"],
    "to the right": ["to the left", "opposite", "adjacent to"],
    # "on": ["off", "beside", "away from"],
    "within": ["without", "outside", "beyond"],
    # "around": ["through", "straight", "beyond"],
    "across": ["along", "beside", "parallel to"],
    "near": ["distant from", "far from", "apart from"],
    "on top of": ["below", "underneath", "beneath"],
    # "through": ["around", "beside", "outside"],
    # "besides": ["excluding", "apart from", "without"],
    # "next to": ["away from", "opposite", "distant from"],
    "beyond reach": ["accessible", "within reach", "close by"],
    "in the midst of": ["outside", "apart from", "away from"],
    "towards": ["away from", "opposite", "retreating from"],
    "upon": ["beneath", "without", "below"]
}

    # Convert sentence_annotated to just words for easier phrase checking
    sentence_words = [word for word, _ in sentence_annotated]

    for augmentation in priority_list:
        if augmentation == "Relation":
            # Check if any spatial relation keyword or phrase is present and return a random augmentation
            for relation, proposals in spatial_relations_map.items():
                if relation in " ".join(sentence_words) and augmentation_counts[augmentation] < max_count:
                    # proposal = random.choice(proposals)
                    augmentation_counts[augmentation] += 1
                    return "Relation", f"{relation}->{proposals}"
        elif augmentation == "Action/Verb" and any(pos == 'VERB' for _, pos in sentence_annotated) and \
                augmentation_counts[augmentation] < max_count:
            augmentation_counts[augmentation] += 1
            return "Action/Verb", None
        elif augmentation == "Attribute/Adjective" and any(pos == 'ADJ' for _, pos in sentence_annotated) and \
                augmentation_counts[augmentation] < max_count:
            augmentation_counts[augmentation] += 1
            return "Attribute/Adjective", None
        elif augmentation == "Object/Noun" and any(pos == 'NOUN' for _, pos in sentence_annotated) and \
                augmentation_counts[augmentation] < max_count:
            augmentation_counts[augmentation] += 1
            return "Object/Noun", None

    return "None", None  # No suitable augmentation identified or all types have reached their limit


if __name__ == '__main__':
    main()