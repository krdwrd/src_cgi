#!/usr/bin/python


import kwdb
import sys
from codecs import open

if len(sys.argv) != 3:
    print "usage: dumppage page_id prefix"
    print "will write prefix.user_id files for every submission of page_id"
    sys.exit(1)

id = int(sys.argv[1])
out = sys.argv[2]

for content, user in kwdb.get_all_submissions(id):
    f = open("%s.%06d" % (out, user,), 'w', 'utf8')
    f.write(content)
    f.close()


