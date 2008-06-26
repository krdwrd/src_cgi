#!/usr/bin/python

import random
import cgi
import krdwrd
import config

fs = cgi.FieldStorage()

corpus = fs.getfirst("corpus", "test")

serial = bool(fs.getfirst("serial"))

pages = krdwrd.get_pages(corpus)

userpages = krdwrd.get_user_tagged(corpus, config.username) or []

page = None

if pages:
    if serial:
        pages = pages or []
        if len(pages) > len(userpages):
            page = sorted(pages)[len(userpages)]
    else:
        pages = set(pages) - set(userpages)
        page = random.sample(pages, 1)[0]

if page:
    loc = "%s/%s" % (config.srcurl(corpus), page)
else:
    loc = config.baseurl + 'bin/stat'

print "Location: %s\n\n" % loc
