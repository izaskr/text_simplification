# run the training and inference for ct-types 1-5
onmt_train --config configs/11/train_rnn_basic.yaml
onmt_train --config configs/12/train_rnn_basic.yaml
onmt_train --config configs/13/train_rnn_basic.yaml
onmt_train --config configs/14/train_rnn_basic.yaml
#onmt_train --config configs/5/train_rnn_basic.yaml

onmt_translate --config configs/11/translate.yaml
onmt_translate --config configs/12/translate.yaml
onmt_translate --config configs/13/translate.yaml
onmt_translate --config configs/14/translate.yaml
#onmt_translate --config configs/5/translate.yaml


# compute the BLUE and SARI scores on the predictions
# 1
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level.txt --sys_sents_path pred/11/rnn_basic.txt -tok none > results/11/rnn.txt

# 2
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin.txt --sys_sents_path pred/12/rnn_basic.txt -tok none > results/12/rnn.txt


# 3
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_tok_bin.txt --sys_sents_path pred/13/rnn_basic.txt -tok none > results/13/rnn.txt

# 4
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_lev_bin.txt --sys_sents_path pred/14/rnn_basic.txt -tok none > results/14/rnn.txt




