from tokenizers import Tokenizer, ByteLevelBPETokenizer
from os.path import join

split_fn = ByteLevelBPETokenizer(
    join("tokenize_model", "{}-vocab.json".format("bpe-bytelevel")),
    join("tokenize_model", "{}-merges.txt".format("bpe-bytelevel"))
)
