#!/usr/bin/python

import kwdb
import sys
from codecs import open

if len(sys.argv) != 3:
    print "Usage: ./addtags.py page_id tagfile"
    sys.exit(1)

page_id, fname = sys.argv[-2:]

fl = [f.strip() for f in file(fname).readlines()]

kwdb.add_annotation(page_id, fl)
kwdb.db.commit()
