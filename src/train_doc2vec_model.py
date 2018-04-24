#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import multiprocessing
import os.path
import sys

from gensim import utils
from gensim.models.doc2vec import TaggedDocument, Doc2Vec


class MyDocs(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        try:
            for line in open(self.filename, 'rb'):
                pieces = utils.to_unicode(line).split()
                tags = pieces[0].split(',')
                words = pieces[1].split(',')
                yield TaggedDocument(words, tags)
        except:
            logging.info('e')


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]

    documents = MyDocs(inp)
    model = Doc2Vec(documents, size=200, window=5, min_count=20, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
