#!/usr/bin/python

import kwdb
import config

if config.path:
    page = int(config.path)
    print "Content-type: text/html\n"
    print kwdb.get_subm_content(page, config.user),
else:
    print "Status: 404\n"
