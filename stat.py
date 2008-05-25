#!/usr/bin/python
import krdwrd
import config

print "Content-type: text/plain\n\n"

for corpus in config.corpora:
    print corpus
    pages = krdwrd.get_user_tagged(corpus, config.username)
    if pages:
      for p in pages:
        print corpus, p

