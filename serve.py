#!/usr/bin/python

import random
import cgi
import krdwrd
import config

fs = cgi.FieldStorage()

corpus = fs.getfirst("corpus", "test")

serial = bool(fs.getfirst("serial"))

pages = krdwrd.get_pages(corpus)

userpages = krdwrd.get_user_tagged(corpus, config.username)

if pages:

  if not serial:
    pages = set(pages) - set(userpages and userpages or [])
    page = random.sample(pages, 1)[0]
  else:
    page = pages[len(userpages)]

  loc = "%s/%s" % (config.srcurl(corpus), page)

else:
    loc = config.baseurl + 'bin/stat'

print "Location: %s\n\n" % loc
