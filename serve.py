#!/usr/bin/python

import random
import cgi
import krdwrd
import config

fs = cgi.FieldStorage()

corpus = fs.getfirst("corpus", "test")

pages = krdwrd.get_pages(corpus)

userpages = krdwrd.get_user_tagged(corpus, config.username)

if pages:
    pages = set(pages) - set(userpages and userpages or [])

if pages:
    page = random.sample(pages, 1)[0]
    loc = "%s/%s" % (config.srcurl(corpus), page)
else:
    loc = config.baseurl + 'bin/stat'

print "Location: %s\n\n" % loc
