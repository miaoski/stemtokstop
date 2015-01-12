# -*- coding: utf8 -*-
import MeCab

SINGLE_WORD_VERBS = ('い', )

def parse(sent):
    t = MeCab.Tagger()
    m = t.parseToNode(sent.encode('utf-8'))
    r = []
    while m:
        if m.feature.split(',', 1)[0] in ('名詞', '動詞', '形容詞', '副詞') and \
           m.surface not in SINGLE_WORD_VERBS:
            r.append(m.surface.decode('utf-8'))
        m = m.next
    return r
