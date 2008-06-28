#!/usr/bin/python

import random
import cgi
import kwdb
import config

fs = cgi.FieldStorage()

corpus = fs.getfirst("corpus", "tutorial")
corpus_id = kwdb.get_corpus(corpus)

serial = bool(fs.getfirst("serial"))

pages = kwdb.pages_left(corpus_id, config.user)

if pages:
    if serial:
        page = pages[0]
    else:
        page = random.sample(pages, 1)[0]
    print "Location: %s/view/%s\n" % (config.baseurl, page, )

else:
    print "Location: %s/stat\n" % (config.baseurl, )
