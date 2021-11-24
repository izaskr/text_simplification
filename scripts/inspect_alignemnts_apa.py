"""
I have noticed some of the alignments in the APA corpus seem very noisy (they are automatic) from 2 perspectives:
- bad semantic match between src and tgt
- many-to-one matches where these tgt matches don't all seem to be a good alignment
"""
import subprocess
import os
import dill
from collections import Counter

# Get the project top folder
TOP_DIR = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                           stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')

alignment_file = os.path.join(TOP_DIR, "data/apa", "apa_alignments")

# load the alignments, create a counter dict
with open(alignment_file, "rb") as f:
    data = dill.load(f)

src_list, tgt_list = [], []
for level, ids in data.items():
    for idx, (src, tgt) in ids.items():
        src_list.append(src)
        tgt_list.append(tgt)

src_counter = Counter(src_list)
tgt_counter = Counter(tgt_list)


def print_multiples(d, part):
    total = 0
    plus1_counts = []
    for sentence, count in d.items():
        if count > 1:
            #print(part, sentence)
            total += 1
            plus1_counts.append(count)
    #print(total, part)
    print("%f percent sentences are appear more than once as %s" % (100*total/sum(d.values()), part))
    print("Average count of non-one counts", sum(plus1_counts)/len(plus1_counts))


print_multiples(src_counter, "source")
print_multiples(tgt_counter, "target")

"""
24.25 % of sentences are appear more than once as source
Average count of non-one counts 2.66

26.89 % of sentences are appear more than once as target
Average count of non-one counts 2.28

Some sentences appear even 6 or 8 times, which can have an effect on the training given such a small corpus
"""

