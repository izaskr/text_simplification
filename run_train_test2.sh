# run the training and inference for ct-types 1-5
onmt_train --config configs/6/train_rnn_basic.yaml
onmt_train --config configs/7/train_rnn_basic.yaml
onmt_train --config configs/8/train_rnn_basic.yaml
onmt_train --config configs/9/train_rnn_basic.yaml
onmt_train --config configs/10/train_rnn_basic.yaml

onmt_translate --config configs/6/translate.yaml
onmt_translate --config configs/7/translate.yaml
onmt_translate --config configs/8/translate.yaml
onmt_translate --config configs/9/translate.yaml
onmt_translate --config configs/10/translate.yaml


# compute the BLUE and SARI scores on the predictions
# 1
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin.txt --sys_sents_path pred/6/rnn_basic.txt -tok none > results/6/rnn.txt

# 2
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_tok_bin.txt --sys_sents_path pred/7/rnn_basic.txt -tok none > results/7/rnn.txt


# 3
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_lev_bin.txt --sys_sents_path pred/8/rnn_basic.txt -tok none > results/8/rnn.txt

# 4
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_tok_bin.txt --sys_sents_path pred/9/rnn_basic.txt -tok none > results/9/rnn.txt


# 5
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_lev_bin.txt --sys_sents_path pred/10/rnn_basic.txt -tok none > results/10/rnn.txt



