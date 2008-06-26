#!/usr/bin/python

import cgi
import krdwrd
import config
from os import path as osp

fs = cgi.FieldStorage()

tags = fs.getfirst("tags")
url = fs.getfirst("url")

def difftags(test, gold):
    if test != gold:
        return gold
    else:
        return "null"


def validate(url, tags):
    # try mapping the url to a (corpus, page) tuple
    parsed = krdwrd.parseurl(url)

    if not parsed:
        return

    corpus, page = parsed
    tags = tags.strip().split()

    goldfile = file(osp.join(config.srcdir(corpus), page + ".tags"))
    goldtags = goldfile.read().strip().split()

    return [difftags(u,g) for u, g in zip(tags, goldtags)]


if tags and url:
    print "Content-Type: text/plain\n"
    v = validate(url, tags)
    print " ".join([str(i) for i in v])

