#!/usr/bin/python

import kwdb
import config

if config.path:
    corpus = int(config.path)
    kwdb.del_all_submissions(config.user, corpus)
    kwdb.db.commit()
    print "Location: %s/stat\n" % (config.baseurl, )
else:
    print "Status: 500\n"
