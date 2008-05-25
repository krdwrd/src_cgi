#!/usr/bin/python

import random
import cgi
import krdwrd
import config

fs = cgi.FieldStorage()

corpus = fs.getfirst("corpus", "test")

pages = krdwrd.get_pages(corpus)

if pages:
    page = random.sample(pages, 1)[0]
    print "Location: %s/%s\n\n" % (config.srcurl(corpus), page)
else:
    print "Content-type: text/plain\n\nNo such corpus: %s" % corpus

