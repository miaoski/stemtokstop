# -*- coding: utf8 -*-
from flask import Flask, request, jsonify
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import json

app = Flask(__name__)
JSON_MIME = 'application/json; charset=utf8'

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
    return px


@app.route("/")
def hello():
    return "Tokenize, stemming, removing stop words.\n"


@app.route("/ru", methods=['POST'])
def post_russian():
    js = russian(request.form['text'])
    return jsonify(text=js)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False     # JSON in UTF-8
    app.config['DEBUG'] = True              # I love debug mode
    app.run(host = '127.0.0.1')
