# -*- coding: utf8 -*-
# Usage:
#   python extract_ja_stopwords.py
#   cat ja_stopword.txt | sort | uniq -c | sort -nr
# Then arbitrarily pick up those high frequency words

from nltk.corpus import knbc
import codecs

f = codecs.open('ja_stopword.txt', 'w', 'utf-8')

for k in knbc.tagged_words():
    x = k[1].split()[2]
    if x not in (u'名詞', u'副詞', u'動詞', u'形容詞'):
        f.write(k[0])
        f.write('\n')

f.close()
