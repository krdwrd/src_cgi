#!/usr/bin/python

import cgi
import config
import kwdb

fs = cgi.FieldStorage()

url = fs.getfirst("url")

def sweep(url):
    page = int(url.rsplit('/', 1)[1])

    #silver = kwdb.get_annotation(page)

    ###
    # dummy output:
    silver = ''
    for i in range(2000):
        silver += "2 " 
    ###

    return silver.split()

if url:
    print "Content-Type: text/plain\n"
    res = " ".join([str(i) for i in sweep(url)])
    print res,
else:
    print "Status: 500\n"
