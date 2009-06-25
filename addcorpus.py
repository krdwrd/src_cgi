#!/usr/bin/python

import kwdb
import sys
import os
import re
from codecs import open

# the default
mime = """text/html"""

if len(sys.argv) == 3:
    name, files = sys.argv[-2:]
elif len(sys.argv) == 4:
    name, files, mime = sys.argv[-3:]
else:
    print "Usage: ./addcorpus.py corpusname filelist [MIME-Type]"
    sys.exit(1)

fl = file(files).readlines()

cid = kwdb.add_corpus(name)

for f in fl:
    url, fname = f.split()
    wclines, wcwords, wcbytes, name = (os.popen('wc '+re.sub('\.[A-Za-z]+','.txt',fname), 'r').read()).split()
    dat = open(fname, 'r', 'utf-8').read()
    #kwdb.add_page(cid, url, dat, mime)
    kwdb.add_page(cid, url, dat, mime, wclines, wcwords, wcbytes)

kwdb.db.commit()
