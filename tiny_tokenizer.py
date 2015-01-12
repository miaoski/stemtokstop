# -*- coding: utf8 -*-
import tinysegmenter
import codecs

# Japanese stop words
f = codecs.open('ja_stopword.txt', 'r', 'utf-8')
JA_STOPWORDS = set([x[:-1] for x in f.readlines()]) # strip \n
f.close()

def parse(sent):
    stem =  tinysegmenter.TinySegmenter() 
    stop = JA_STOPWORDS
    tx = stem.tokenize(sent)
    px = [x for x in tx if x not in stop]
    return px
