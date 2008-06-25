#!/usr/bin/python

import cgi

fs = cgi.FieldStorage()

tags = fs.getfirst("tags")
url = fs.getfirst("url")


if tags and url:
    print "Content-Type: text/plain\n"
    print " ".join([str(i % 3 + 1) for i in range(1000)])

