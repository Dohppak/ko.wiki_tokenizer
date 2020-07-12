import six
import logging
import time
import sys
from gensim.corpora import WikiCorpus
import json
import os
# with open(os.path.join(hparams.corpus_path,'music_token.json')) as file_object:
#     newdict = json.load(file_object)

def main():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    
    output = open("./wiki_dump/Ko_Wiki_Corpus.txt", 'w')
    space = " "
    i = 0
    wiki = WikiCorpus("./wiki_dump/kowiki-latest-pages-articles.xml.bz2", lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        sentence = space.join(text)
        output.write(sentence + "\n")

        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    print("Finsih Make Custom Token")

if __name__ == "__main__":
	main()
