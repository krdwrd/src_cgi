#!/usr/bin/python

import cgi
import config
import kwdb

fs = cgi.FieldStorage()

tags = fs.getfirst("tags")
url = fs.getfirst("url")

def difftags(test, gold):
    if test != gold:
        return gold
    else:
        return gold + "-l"


def validate(url, tags):
    page = int(url.rsplit('/', 1)[1])

    gold = kwdb.get_annotation(page)
    tags = tags.strip().split()

    goldtags = gold.split()

    return [difftags(u,g) for u, g in zip(tags, goldtags)]


if tags and url:
    print "Content-Type: text/plain\n"
    v = validate(url, tags)
    res = " ".join([str(i) for i in v])
    print res,
else:
    print "Status: 500\n"
