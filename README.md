README
======
stemtokstop = stemmer + tokenizer + remove stop words.  It's nothing special, but a simple application of NLTK wrapped with Flask.


INSTALL
=======
    $ pip install nltk
    $ pip install snowballstemmer  # 1.2.0 supports Turkish
    $ python
    >>> import nltk
    >>> nltk.download() # And download all
    >>> ^D
    $ python stemtokstop.py

For Japanese stemmer, I chose Masato Hagiwara's [TinySegmenter] (https://code.google.com/p/mhagiwara/source/browse/trunk/nltk/jpbook/tinysegmenter.py).  It applies BSD License, so I keep a copy here.

If you like to have a more precise result in Japanese, install [MeCab] (http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html).  Make it UTF-8 only.  stemtokstop will use MeCab in place of TinySegmenter.


TEST
====
Run `stemtokstop.py` in one terminal, and run `test.py` in another.
    $ python test.py

You should see Sent: and Recv:.  Use your linguistic knowledge to justify if the result is satisfactory.


WHAT IF I DON'T LIKE IT?
========================
Open an issue, or better, submit a pull request.

I'm not satisfied with the current output, because I'd like them to be in Noun-stem and not the stems in a stemmer.  For example, `europe`, not `europ` for Europe.  It's possible to find another stemmer.

As for Japanese stop words, I use a heuristic method to enumerate them.  Japanese, as well as Chinese, needs to be tagged to get high accuracy.  Arbitrarily removing stop words (like the implementation here) results in losing meaningful words.


LICENSE
=======
Apache License 2.0.  Please refer to `LICENSE`.
* `tinysegmenter.py` is written by Masato Hagiwara (萩原 正人).  Please refer to [his blog] (http://lilyx.net/tinysegmenter-in-python/) for his excellent Japanese tokenizer.
* Release early, release often.
