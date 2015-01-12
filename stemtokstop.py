# -*- coding: utf8 -*-
from flask import Flask, request, jsonify, abort
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import json

app = Flask(__name__)
JSON_MIME = 'application/json; charset=utf8'

def dutch(sent):
    pass

def finnish(sent):
    pass

def german(sent):
    pass

def italian(sent):
    pass

def portuguese(sent):
    pass

def spanish(sent):
    pass

def turkish(sent):
    pass

def danish(sent):
    pass

def english(sent):
    pass

def french(sent):
    pass

def hungarian(sent):
    pass

def norwegian(sent):
    pass

def russian(sent):
    stem = SnowballStemmer('russian')
    stop = stopwords.words('russian')
    tx  = PunktWordTokenizer().tokenize(sent) 
    mx = map(stem.stem, tx)
    px = [x for x in mx if x not in stop]
    return px

def swedish(sent):
    pass

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
               'sv': swedish}

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
