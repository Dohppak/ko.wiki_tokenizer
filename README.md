# ko.wiki_tokenizer

한국어 Byte Level BPE를 위한 Repository 입니다.

### train from scratch
```
cd wiki_dump
wget https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles.xml.bz2
cd ../python wiki_preprocessing.py
python train.py --files="./wiki_dump/Ko_Wiki_Corpus.txt" --out ="tokenize_model" --name="bpe-bytelevel"
```

### load Collable fn and Apply pandas series
```
from split_fn import split_fn
list_of_tokens = df["document"].apply(split_fn.encode).map(lambda x: x.tokens).tolist()
```