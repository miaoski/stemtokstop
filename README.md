README
======
stemtokstop = stemmer + tokenizer + remove stop words.  It's nothing special, but a simple application of NLTK wrapped with Flask.


INSTALL
=======
    $ pip install nltk
    $ python
    >>> import nltk
    >>> nltk.download() # And download all
    >>> ^D
    $ python stemtokstop.py


TEST
====
Run `stemtokstop.py` in one terminal, and run `test.py` in another.
    $ python test.py

You should see Sent: and Recv:.  Use your linguistic knowledge to justify if the result is satisfactory.


WHAT IF I DON'T LIKE IT?
========================
Open an issue, or better, submit a pull request.

I'm not satisfied with the current output, because I'd like them to be in Noun-stem and not the stems in a stemmer.  For example, `europe`, not `europ` for Europe.  It's possible to find another stemmer, anyhow.

I can't find a Turkish stemmer.  You know a working one, please open an issue.


LICENSE
=======
Apache License 2.0.  Please refer to `LICENSE`.

Release early, release often.
