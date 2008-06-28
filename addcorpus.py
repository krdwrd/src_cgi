import kwdb
import sys
from codecs import open

if len(sys.argv) != 3:
    print "Usage: ./addcorpus.py corpusname filelist"
    sys.exit(1)

name, files = sys.argv[-2:]

fl = file(files).readlines()

cid = kwdb.add_corpus(name)

for f in fl:
    url, fname = f.split()
    dat = open(fname, 'r', 'utf-8').read()
    kwdb.add_page(cid, url, dat)

kwdb.db.commit()
