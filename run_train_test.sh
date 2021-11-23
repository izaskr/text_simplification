# run the training and inference for ct-types 1-5
onmt_train --config configs/1/train_rnn_basic.yaml
onmt_train --config configs/2/train_rnn_basic.yaml
onmt_train --config configs/3/train_rnn_basic.yaml
onmt_train --config configs/4/train_rnn_basic.yaml
onmt_train --config configs/5/train_rnn_basic.yaml

onmt_translate --config configs/1/translate.yaml
onmt_translate --config configs/2/translate.yaml
onmt_translate --config configs/3/translate.yaml
onmt_translate --config configs/4/translate.yaml
onmt_translate --config configs/5/translate.yaml


# compute the BLUE and SARI scores on the predictions
# 1
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_tok_bin_lev_bin.txt --sys_sents_path pred/1/rnn_basic.txt -tok none > results/1/rnn.txt

# 2
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_tok_bin.txt --sys_sents_path pred/2/rnn_basic.txt -tok none > results/2/rnn.txt


# 3
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_lev_bin.txt --sys_sents_path pred/3/rnn_basic.txt -tok none > results/3/rnn.txt

# 4
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_tok_bin_lev_bin.txt --sys_sents_path pred/4/rnn_basic.txt -tok none > results/4/rnn.txt


# 5
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_tok_bin_lev_bin.txt --sys_sents_path pred/5/rnn_basic.txt -tok none > results/5/rnn.txt



