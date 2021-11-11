"""
Extract the features from the complex-simple alignments for two purposes:
- general insight into the data
- for seq2seq models: prepend them as control tokens, but first put them into bins ot avoid sparsity

Control tokens:
- max dependency tree depth: but this works if the alignment is one-sentence -> one-sentence, which doesn't hold for
    this dataset. The sentence count ratio can be used instead
- Levenshtein similarity
- character count ratio
- word frequency: focusing on the more rare words (Martin et al. third quartile), but think which corpus should be used

This about these as well:
- lexical density: ratio: number of lexical items in relation to the total number of words
- Laser sentence embeddings?
- faiss tool for similarity: is there support for German?

The extracted feature values are floats. Martin et al. 2020 (ACCESS) treat them as follows:
Ratios are discretized into bins of fixed width of 0.05 in our experiments and capped to a maximum ratio of 2.
Control tokens are then included in the vocabulary (40 unique values per control token)

"""
import random
import dill, json
import numpy as np
import spacy
import Levenshtein
import matplotlib.pyplot as plt
import seaborn as sns

nlp = spacy.load("de_core_news_md")


def load_binary(path_to_bin):
    with open(path_to_bin, "rb") as f:
        data = dill.load(f)
    print("Loaded ", path_to_bin)
    return data


def load_feature_bins(path_feature_bins):
    with open(path_feature_bins, "r") as f:
        data = json.load(f)
    print("Loaded ", path_feature_bins)
    return data


def sentence_and_token_ratio(complex, simple):

    docc, docs = nlp(complex), nlp(simple)
    # count the number of sentences in the strings
    lenc, lens = sum([1 for s in docc.sents]), sum([1 for g in docs.sents])
    sent_ratio = lens / lenc

    # count the number of tokens in the strings, ignore the empty strings (somehow not entirely ignored by
    # the spacy tokenizer?)
    tokc, toks = len([t for t in docc if t.text.strip()]), len([t for t in docs if t.text.strip()])
    tok_ratio = toks / tokc

    #print(tok_ratio)

    return sent_ratio, tok_ratio


def character_ratio(complex, simple):
    """
    Source/target character count
    """
    return len(simple) / len(complex)


def levenshtein_ratio(complex, simple):
    """
    This function returns a ratio (between 0 and 1), which is not the same as Levenshtein distance!
    See this documentation https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-ratio
    """
    return Levenshtein.ratio(complex, simple)


def word_freq_ratio(complex, simple):
    pass


def lexical_density(complex, simple):
    pass


def histogram(x_axis, name):
    # plt.hist(x_axis)
    # plt.ylabel('Count')
    # plt.xlabel('Control token values')
    # plt.title(name)
    # plt.savefig("/home/skrjanec/text_simplification/extracted_features/" + name + "bins_apa.png")
    # plt.show()
    fig = sns.histplot(x_axis)
    plt.xlabel("Control token values")
    plt.ylabel("Counts")
    plt.title(name)
    plt.savefig("/home/skrjanec/text_simplification/extracted_features/" + name + "_bins_apa.png")
    plt.show()


def get_bin_value(feature_name, bins, feature_value):
    relevant_bins = np.array(bins[feature_name]["bins"])
    ind = np.digitize(np.array([feature_value]), relevant_bins, right=True)[0] # select first and only item in the array
    bin_value = bins[feature_name]["bins"][ind] if ind < len(bins[feature_name]["bins"]) else bins[feature_name]["bins"][ind-1]

    return np.round(bin_value, 2)

def collect_features(data, feature_bins, write=False):
    sent_ratios, tok_ratios, lev_ratios, char_ratios = [], [], [], []
    alignments_features = []
    for level, alignments in data.items():
        for idx, (comp, simp) in alignments.items():
            sent_r, tok_r = sentence_and_token_ratio(comp, simp)
            lev_ratio = levenshtein_ratio(comp, simp)
            char_ratio = character_ratio(comp, simp)
            #sent_ratios.append(sent_r), tok_ratios.append(tok_r)
            #lev_ratios.append(lev_ratio), char_ratios.append(char_ratio)

            # for the feature value of this alignment, get the bin value and store it
            lev_bin = get_bin_value("levenshtein_ratio", feature_bins, lev_ratio)
            #print("LEVENSHETIN raw value, bin value", lev_ratio, lev_bin)

            char_bin = get_bin_value("character_ratio", feature_bins, char_ratio)
            #print("CHAR raw value, bin value", char_ratio, char_bin)

            tok_bin = get_bin_value("token_ratio", feature_bins, tok_r)
            #print("TOKEN raw value, bin value", tok_r, tok_bin)

            alignments_features.append((level, char_bin, tok_bin, lev_bin, comp, simp))

            tok_ratios.append(tok_bin)
            lev_ratios.append(lev_bin), char_ratios.append(char_bin)



    # plot these features real quick
    #histogram(lev_ratios, "Levenshtein_ratio")
    #input("... next histogram")
    #histogram(sent_ratios, "Sentence_count_ratio")
    #input("... next histogram")
    #histogram(tok_ratios, "Token_count_ratios")
    #input("... next histogram")
    #histogram(char_ratios, "Character_count_ratios")
    #print("end of feature extraction and plotting")

    # dump the features into a separate file for inspection DONE
    # features = {"levenshtein_ratio": lev_ratios, "character_ratio": char_ratios,
    #             "token_ratio": tok_ratios}
    # with open("/home/skrjanec/text_simplification/extracted_features/features.json", "w") as fout:
    #     json.dump(features, fout)

    # conditionally write the complex-simple alignments and features into a file
    if write:
        random.shuffle(alignments_features)
        out_dict = {"content_info": [("level", "char_bin", "tok_bin", "lev_bin", "complex", "simple")],
                    "data": alignments_features}
        with open("/home/skrjanec/text_simplification/data/apa/features_and_text.json", "w") as fout:
            json.dump(out_dict, fout)
        # TODO: WRITE several versions of the data into files: with all features, with some, with none
        # create a split, write the splits into txt files



german_alignments = load_binary("/home/skrjanec/text_simplification/data/apa/apa_alignments")
feature_bins = load_feature_bins("/home/skrjanec/text_simplification/extracted_features/features_bins.json")
collect_features(german_alignments, feature_bins, True)

