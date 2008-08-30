#!/usr/bin/python


import kwdb
import sys
from codecs import open

if len(sys.argv) < 3:
    print "usage: dumppage page_id output"
    print "write page content to ``output`` file"
    sys.exit(1)

id = int(sys.argv[1])
out = sys.argv[2]

content = kwdb.get_page_content(id)
f = open(out, 'w', 'utf8')
f.write(content)
f.close()
