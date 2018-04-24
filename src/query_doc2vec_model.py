#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from decimal import Decimal
from gensim.models import Doc2Vec

if __name__ == '__main__':
    # check and process input arguments
    if len(sys.argv) < 4:
        sys.exit(1)
    modelfile, dishfile, dishSimfile = sys.argv[1:4]

    out = open(dishSimfile, 'w', encoding='utf-8')

    model = Doc2Vec.load(modelfile)
    with open(dishfile, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)
            sims = ""
            try:
                sims = model.docvecs.most_similar(line.strip(), topn=5)
            except:
                continue
            out.write(line.strip() + ":")
            for name, degree in sims:
                out.write(name + ":" + str(Decimal(degree).quantize(Decimal('0.00'))) + '\t')
            out.write("\n")
    out.close()
    # sims是一个tuples,(index_of_document, similarity)
