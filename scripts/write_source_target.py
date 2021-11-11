"""
Write into files the source and target sides for text simplification with or without control tokens

Based on the file with features and alignments: data/apa/features_and_text.json

Create a split (Saeuberli et al. 2020) didn't create a fixed split:
    'Moreover, each model type was trained three times, with three different random seeds for
    shuffling and splitting the training and validation set, in order to reach statistical significance.'

I will create a fixed split for now: 75 / 10 / 15 for  the train / val / test set.
"""

import json
import random
import more_itertools
import os

random.seed(3)

with open("/home/skrjanec/text_simplification/data/apa/features_and_text.json", "r") as f:
    data = json.load(f)

out_dir = "/home/skrjanec/text_simplification/data/apa/source_target"

features = data["content_info"][0][:-2]  # the last two are the complex and simple strings
feature_indx = {feature: i for i, feature in enumerate(features)}
feature_special_tokens = {"level":"Level", "char_bin":"CharRatio", "tok_bin":"TokenRatio", "lev_bin":"LevRatio",
                          "word_freq":"WordFreq"}

# create feature combinations: no features, all features, only 2 etc.
combinations = list(more_itertools.powerset(features))

# shuffle and split the data and write the target sides
random.shuffle(data["data"])


def write_all():
    size_train = int(len(data["data"]) * 0.75)
    size_val = int(len(data["data"]) * 0.10)
    size_test = len(data["data"]) - size_train - size_val
    print("Number of aligned complex-simple strings in train %d, val %d, and test %d" %
          (size_train, size_val, size_test))

    train, val, test = data["data"][:size_train], data["data"][size_train:size_train+size_val], data["data"][-size_test:]

    print("After splitting: ")
    print("train %d, val %d, test %d" % (len(train), len(val), len(test)))

    def write_target(splt, name):
        """
        Write the target sides into files
        :param splt: list of lists with data points
        :param name: str, the name of the split
        :return:
        """
        with open(os.path.join(out_dir, "target_" + name + ".txt"), "w") as fout:
            for single_instance in splt:
                fout.write(single_instance[-1] + "\n")

        print("\t Wrote file", os.path.join(out_dir, name+".txt"))


    def write_source(selected_features, data, split_name):
        """
        :param selected_features: a tuple of features, can be empty too
        :param data: a list of lists
        :return:
        """
        selected_idx = [feature_indx[fe] for fe in selected_features]
        name = "source_" + split_name + "_" + "_".join(selected_features) if selected_features else "source_none_" + split_name
        with open(os.path.join(out_dir, name+".txt"), "w") as fout:
            for single_instance in data:
                end_string = single_instance[-2]  # complex (source)

                if not selected_features:
                    fout.write(end_string + "\n")
                    continue

                for feature in selected_features:
                    j = feature_indx[feature]
                    special_tok = feature_special_tokens[feature]
                    # get the value of the feature and format it such that <SpecTok_0.4>
                    #import pdb; pdb.set_trace()
                    added_text = "<" + special_tok + "_" + str(single_instance[j]) + ">"
                    end_string = added_text + " " + end_string

                fout.write(end_string + "\n")


                #fout.write(single_instance[-1] + "\n")

    for (data_split, split_name) in [(train, "train"), (val, "val"), (test, "test")]:
        write_target(data_split, split_name)
        for c in combinations:
            write_source(c, data_split, split_name)


write_all()
