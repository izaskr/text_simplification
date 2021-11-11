"""
Preprocess the APA corpus (APA_sentence-aligned_LHA) with German parallel simple-complex data
The alignments are automatic. Simple sides are in files *.simplede, the complex in .de
For two different language proficiency levels: A2-OR and B1-OR

Read in the data, compare the complex-simple pairs: token count, sentence count. Compare the two levels
Write the parallel sentences in two files: a2 and b1.
"""

import os
import spacy
import dill
import numpy as np

nlp = spacy.load('de_core_news_md')


def read_in_from_folders(path_to_folder, level):
    # read in the file names
    fprefixes = set()
    sent_ratios, token_ratios = [], []
    parallels = dict()
    files = sorted(os.listdir(path_to_folder))

    for fname in files:
        prefix = fname.split(".")[0][:-3] if fname.split(".")[0].endswith("_A2") or fname.split(".")[0].endswith("_B1") else fname.split(".")[0]
        if prefix in fprefixes:
            continue

        sentc = open(os.path.join(path_to_folder, prefix+".de")).read().splitlines()
        sents = open(os.path.join(path_to_folder, prefix+"_"+level.upper()+".simpde")).read().splitlines()
        fprefixes.add(prefix)
        assert len(sentc) == len(sents)

        # for every aligned pair, count the tokens and sentences and the ratio between these numbers
        for (sc, ss) in zip(sentc, sents):
            docc, docs = nlp(sc), nlp(ss)
            # count the number of sentences in the strings
            lenc, lens = sum([1 for s in docc.sents]), sum([1 for g in docs.sents])
            sent_ratio = lenc/lens
            sent_ratios.append(sent_ratio)

            # count the number of tokens in the strings, ignore the empty strings (somehow not entirely ignored by
            # the spacy tokenizer?)
            tokc, toks = len([t for t in docc if t.text.strip()]), len([t for t in docs if t.text.strip()])
            tok_ratio = tokc/toks
            token_ratios.append(tok_ratio)

            # put the alignments in the dict
            parallels[len(parallels)] = (sc, ss)

        print("Number of processed alignment files", len(fprefixes))

    return parallels, sent_ratios, token_ratios


def dump_corpus_binary(dictionary, path_fname):
    with open(path_fname, "wb") as out:
        dill.dump(dictionary, out)
    print("wrote dill binary file into " + path_fname)


def get_simple_stats(level, sentence_r, token_r):
    print("Corpus %s" % level)
    print("Ratios complex/simple:")
    print("Maximal, minimal and average ratio in sentence count %d %d %d" % (max(sentence_r),
                                                                             min(sentence_r), np.mean(sentence_r)))

    print("Maximal, minimal and average ratio in token count %d %d %d" % (max(token_r),
                                                                          min(token_r), np.mean(token_r)))


a2_alignments, a2_sent_ratios, \
a2_token_ratios = read_in_from_folders("/home/skrjanec/text_simplification/data/APA_sentence-aligned_LHA/A2-OR", "a2")

b1_alignments, b1_sent_ratios, \
b1_token_ratios = read_in_from_folders("/home/skrjanec/text_simplification/data/APA_sentence-aligned_LHA/B1-OR", "b1")


dump_corpus_binary({"a2": a2_alignments, "b1": b1_alignments}, "/home/skrjanec/text_simplification/data/apa/apa_alignments")

get_simple_stats("a2", a2_sent_ratios, a2_token_ratios)
get_simple_stats("b1", b1_sent_ratios, b1_token_ratios)



