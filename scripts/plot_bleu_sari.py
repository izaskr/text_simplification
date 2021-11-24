"""
Crawl the files in results/*/.txt to get the BLEU and SARI scores.
Plot them as bar charts

15 control token settings: 1 - all, 15 - none
"""
import os
import subprocess
from ast import literal_eval
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json


# Get the project top folder
TOP_DIR = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                           stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')

results_dir = os.path.join(TOP_DIR, "results")

folders = sorted(os.listdir(results_dir))
folders_str = [str(i) for i in range(1, len(folders)+1) if str(i) in folders]  # ["1", "2" ... "15"]
assert len(folders) == len(folders_str)


def get_bleu_sari(experiment_folder, experiment_id):
    result = {experiment_id: {"BLEU_copy": 0, "BLEU": 0, "SARI_copy": 0, "SARI": 0}}
    f1, f2 = os.path.join(experiment_folder, "rnn.txt"), os.path.join(experiment_folder, "rnn_copy.txt")
    with open(f1) as f:
        lines = f.readlines()
        d = literal_eval(lines[0])
        result[experiment_id]["BLEU"] = d["bleu"]
        result[experiment_id]["SARI"] = d["sari"]
        bleu = d["bleu"]
        sari = d["sari"]

    with open(f2) as f:
        lines = f.readlines()
        d = literal_eval(lines[0])
        result[experiment_id]["BLEU_copy"] = d["bleu"]
        result[experiment_id]["SARI_copy"] = d["sari"]
        bleu_copy = d["bleu"]
        sari_copy = d["sari"]

    return [bleu, "BLEU"], [bleu_copy, "BLEU_COPY"], [sari, "SARI"], [sari_copy, "SARI_COPY"]


exp2ct = {"1": "level,charR,tokR,Lev",
          "2": "level,charR,tokR",
          "3": "level,charR,Lev",
          "4": "level,tokR,Lev",
          "5": "charR,tokR,Lev",
          "6": "level,charR",
          "7": "level,tokR",
          "8": "level,Lev",
          "9": "charR,tokR",
          "10": "charR,Lev",
          "11": "level",
          "12": "charR",
          "13": "tokR",
          "14": "Lev", "15": "none"}

if __name__ == "__main__":
    results_list = []
    for exp_id in folders_str:
        res = get_bleu_sari(os.path.join(results_dir, exp_id), exp_id)
        for score_name in res:
            score_name.append(exp_id)
            score_name.append(exp2ct[exp_id])
            results_list.append(tuple(score_name))

    df = pd.DataFrame(results_list, columns=["value", "metric", "Experiment", "Experiment_ControlTokens"])

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    palette = {"BLEU": "navy", "BLEU_COPY": "royalblue", "SARI": "darkorange", "SARI_COPY": "sandybrown"}
    sns.barplot(x="Experiment_ControlTokens", hue="metric", y="value", data=df, palette=palette)
    # Put the legend out of the figure
    plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
    plt.yticks(np.arange(0, max(df.value)+2, 2))
    plt.xticks(rotation=70)

    plt.show()






