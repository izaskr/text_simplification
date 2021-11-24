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
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_tok_bin_lev_bin.txt --sys_sents_path pred/1/rnn_basic_copy.txt -tok none > results/1/rnn_copy.txt

# 2
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_tok_bin.txt --sys_sents_path pred/2/rnn_basic_copy.txt -tok none > results/2/rnn_copy.txt

# 3
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin_lev_bin.txt --sys_sents_path pred/3/rnn_basic_copy.txt -tok none > results/3/rnn_copy.txt

# 4
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_tok_bin_lev_bin.txt --sys_sents_path pred/4/rnn_basic_copy.txt -tok none > results/4/rnn_copy.txt

# 5
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_tok_bin_lev_bin.txt --sys_sents_path pred/5/rnn_basic_copy.txt -tok none > results/5/rnn_copy.txt

# run the training and inference for ct-types 6-10
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
easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_char_bin.txt --sys_sents_path pred/6/rnn_basic_copy.txt -tok none > results/6/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_tok_bin.txt --sys_sents_path pred/7/rnn_basic_copy.txt -tok none > results/7/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level_lev_bin.txt --sys_sents_path pred/8/rnn_basic_copy.txt -tok none > results/8/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_tok_bin.txt --sys_sents_path pred/9/rnn_basic_copy.txt -tok none > results/9/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin_lev_bin.txt --sys_sents_path pred/10/rnn_basic_copy.txt -tok none > results/10/rnn_copy.txt

# run the training and inference for ct-types 11-15
onmt_train --config configs/11/train_rnn_basic.yaml
onmt_train --config configs/12/train_rnn_basic.yaml
onmt_train --config configs/13/train_rnn_basic.yaml
onmt_train --config configs/14/train_rnn_basic.yaml
onmt_train --config configs/15/train_rnn_basic.yaml

onmt_translate --config configs/11/translate.yaml
onmt_translate --config configs/12/translate.yaml
onmt_translate --config configs/13/translate.yaml
onmt_translate --config configs/14/translate.yaml
onmt_translate --config configs/15/translate.yaml


# compute the BLUE and SARI scores on the predictions

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_level.txt --sys_sents_path pred/11/rnn_basic_copy.txt -tok none > results/11/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_char_bin.txt --sys_sents_path pred/12/rnn_basic_copy.txt -tok none > results/12/rnn_copy.txt


easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_tok_bin.txt --sys_sents_path pred/13/rnn_basic_copy.txt -tok none > results/13/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_test_lev_bin.txt --sys_sents_path pred/14/rnn_basic_copy.txt -tok none > results/14/rnn_copy.txt

easse evaluate -m "bleu,sari" -t custom --refs_sents_paths data/apa/source_target/target_test.txt --orig_sents_path data/apa/source_target/source_none_test.txt --sys_sents_path pred/15/rnn_basic_copy.txt -tok none > results/15/rnn_copy.txt


