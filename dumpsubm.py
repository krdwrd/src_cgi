#!/usr/bin/python


import kwdb
import sys
from codecs import open

if len(sys.argv) < 3:
    print "usage: dumppage page_id prefix [user_id]"
    print "write ``prefix``.user_id files for every submission of ``page_id``"
    print "OR just ``prefix`` if user_id is given"
    sys.exit(1)

id = int(sys.argv[1])
out = sys.argv[2]
user_id = len(sys.argv) > 3 and sys.argv[3] or None

def dropall():
    for content, user in kwdb.get_all_submissions(id):
        f = open("%s.%06d" % (out, user,), 'w', 'utf8')
        f.write(content)
        f.close()

def dropuser():
    content = kwdb.get_subm_content(id, user_id)
    f = open(out, 'w', 'utf8')
    f.write(content)
    f.close()

if not user_id:
    dropall()
else:
    dropuser()
