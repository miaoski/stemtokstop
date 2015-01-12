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

For Japanese stemmer, I chose [MeCab] (http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html) and IPA 辞書.  Please follow its installation guide.


TEST
====
Run `stemtokstop.py` in one terminal, and run `test.py` in another.
    $ python test.py

You should see Sent: and Recv:.  Use your linguistic knowledge to justify if the result is satisfactory.


WHAT IF I DON'T LIKE IT?
========================
Open an issue, or better, submit a pull request.

I'm not satisfied with the current output, because I'd like them to be in Noun-stem and not the stems in a stemmer.  For example, `europe`, not `europ` for Europe.  It's possible to find another stemmer, anyhow.


LICENSE
=======
Apache License 2.0.  Please refer to `LICENSE`.

Release early, release often.
