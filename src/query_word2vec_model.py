#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gensim
import sys

if __name__ == '__main__':
    # check and process input arguments
    if len(sys.argv) < 3:
        sys.exit(1)
    file, word = sys.argv[1:3]

    model = gensim.models.Word2Vec.load_word2vec_format(file, binary=False)
    print(model.most_similar(word))
