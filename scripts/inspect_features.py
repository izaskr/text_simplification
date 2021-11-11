"""
Inspect the extracted features and create bins with numpy digitize
"""
import json
import numpy as np
import matplotlib.pyplot as plt


path_features = "/home/skrjanec/text_simplification/extracted_features/features.json"
path_bins_out = "/home/skrjanec/text_simplification/extracted_features/features_bins.json"


def load_features(path):
    with open(path) as f:
        data = json.load(f)
    return data

def create_bins(feature_name, list_values, step=0.08):
    x = np.array(list_values)
    print("Feature: ", feature_name)
    print("Min %f, max %f, mean %f" % (np.min(x), np.max(x), np.mean(x)))
    # ROUND THE EXTRACTED FEATURES TO 2 DECIMALS
    x = np.array([np.round(v, 2) for v in x])
    bins = np.arange(np.min(x), np.max(x), step)
    ids = np.digitize(x, bins, right=True)

    # replace raw feature values with its bins
    x_binned = [bins[ids[n]] if ids[n] < bins.size else bins[ids[n]-1] for n in range(x.size)]
    print("Number of bins: %d" % len(bins))
    assert len(x) == len(x_binned)

    return bins


features_bins = {}

for feat, values in load_features(path_features).items():
    steps = {"levenshtein_ratio": 0.08, "character_ratio": 0.1, "token_ratio": 0.1}
    bins = create_bins(feat, values, steps[feat])
    features_bins[feat] = {"values":values, "bins":bins.tolist()}

with open(path_bins_out, "w") as fout:
    json.dump(features_bins, fout)
    print("Wrote ", path_bins_out)


