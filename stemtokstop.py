# -*- coding: utf8 -*-
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# ISO639-1
NLTKlanguages={'NL': "dutch",
               'FI': "finnish",
               'DE': "german",
               'IT': "italian",
               'PT': "portuguese",
               'ES': "spanish",
               'TR': "turkish",
               'DA': "danish",
               'EN': "english",
               'FR': "french",
               'HU': "hungarian",
               'NO': "norwegian",
               'RU': "russian",
               'SV': "swedish"}

def russian(sent):
    stem = SnowballStemmer('russian')
    stop = stopwords.words('russian')
    tx  = PunktWordTokenizer().tokenize(sent) 
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return ' '.join(px)

if __name__ == '__main__':
    rus_text = u'Пролетариат использует свое политическое господство для того, чтобы вырвать у буржуазии шаг за шагом весь капитал, централизовать все орудия производства в руках государства, т. е. пролетариата, организованного как господствующий класс, и возможно более быстро увеличить сумму производительных сил.'
    print rus_text
    print russian(rus_text)
