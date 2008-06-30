#!/usr/bin/python

import kwdb
import config

if config.path:
    page = int(config.path)
    kwdb.del_submission(config.user, page)
    kwdb.db.commit()
    print "Location: %s/stat\n" % (config.baseurl, )
else:
    print "Status: 500\n"
