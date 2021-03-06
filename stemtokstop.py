# -*- coding: utf8 -*-
from flask import Flask, request, jsonify, abort
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import snowballstemmer
import json
try:
    import MeCab
    import mecab_tokenizer as jpn_tok
except ImportError:
    import tiny_tokenizer as jpn_tok

app = Flask(__name__)
JSON_MIME = 'application/json; charset=utf8'

def dutch(sent):
    stem = SnowballStemmer('dutch')
    stop = stopwords.words('dutch')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def finnish(sent):
    stem = SnowballStemmer('finnish')
    stop = stopwords.words('finnish')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def german(sent):
    stem = SnowballStemmer('german')
    stop = stopwords.words('german')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def italian(sent):
    stem = SnowballStemmer('italian')
    stop = stopwords.words('italian')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def portuguese(sent):
    stem = SnowballStemmer('portuguese')
    stop = stopwords.words('portuguese')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def spanish(sent):
    stem = SnowballStemmer('spanish')
    stop = stopwords.words('spanish')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def turkish(sent):
    # No turkish stemmer in NLTK
    stem = snowballstemmer.stemmer('turkish')
    stop = stopwords.words('turkish')
    tx  = word_tokenize(sent)
    mx = stem.stemWords(tx)
    px = [x for x in mx if x not in stop]
    return px

def danish(sent):
    stem = SnowballStemmer('danish')
    stop = stopwords.words('danish')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def english(sent):
    stem = SnowballStemmer('english')
    stop = stopwords.words('english')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def french(sent):
    stem = SnowballStemmer('french')
    stop = stopwords.words('french')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def hungarian(sent):
    stem = SnowballStemmer('hungarian')
    stop = stopwords.words('hungarian')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def norwegian(sent):
    stem = SnowballStemmer('norwegian')
    stop = stopwords.words('norwegian')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def russian(sent):
    stem = SnowballStemmer('russian')
    stop = stopwords.words('russian')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def swedish(sent):
    stem = SnowballStemmer('swedish')
    stop = stopwords.words('swedish')
    tx  = word_tokenize(sent)
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def chinese_t(sent):
    pass

def chinese_s(sent):
    pass

def japanese(sent):
    return jpn_tok.parse(sent)

# ISO639-1
NLTKlanguages={'nl': dutch,
               'fi': finnish,
               'de': german,
               'it': italian,
               'pt': portuguese,
               'es': spanish,
               'tr': turkish,
               'da': danish,
               'en': english,
               'fr': french,
               'hu': hungarian,
               'no': norwegian,
               'ru': russian,
               'sv': swedish,
               'cht': chinese_t,
               'chs': chinese_s,
               'ja': japanese,
               }

@app.route("/")
def hello():
    return "Tokenize, stemming, removing stop words.\n"


@app.route("/<lang>", methods=['POST'])
def post_lang(lang):
    lang = lang.lower()
    if lang not in NLTKlanguages:
        abort(404)
    func = NLTKlanguages[lang]
    js = func(request.form['text'])
    return jsonify(text=js)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False     # JSON in UTF-8
    app.config['DEBUG'] = True              # I love debug mode
    app.run(host = '127.0.0.1')
