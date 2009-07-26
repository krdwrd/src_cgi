#!/usr/bin/python

import config
import cgi
import kwdb

fs = cgi.FieldStorage()

html = fs.getfirst("html")
url = fs.getfirst("url")

if html and url:
    try:
        page = int(url.rsplit('/', 2)[1])
    except(ValueError):
        page = int(url.rsplit('/', 1)[1])

    kwdb.add_submission(config.user, page, html)
    kwdb.db.commit()
    print "Content-Type: text/plain\n"
else:
    print "Status: 500\n"


