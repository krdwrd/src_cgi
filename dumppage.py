#!/usr/bin/python

# usage: dumppage page_id prefix
# will write prefix.user_id files for every submission of page_id

import kwdb
import sys
from codecs import open

id = int(sys.argv[1])
out = sys.argv[2]

for content, user in kwdb.get_all_submissions(id):
    f = open("%s.%06d" % (out, user,), 'w', 'utf8')
    f.write(content)
    f.close()


