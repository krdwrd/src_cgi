#!/usr/bin/python

import kwdb
import sys
from codecs import open

if len(sys.argv) == 3:
    user_id, files = sys.argv[-2:]
else:
    print "Usage: ./addsubm.py user_id filelist"
    sys.exit(1)

fl = file(files).readlines()

for f in fl:
    id, fname = f.split()
    dat = open(fname, 'r', 'utf-8').read()
    kwdb.add_submission(user_id, id, dat)

kwdb.db.commit()
