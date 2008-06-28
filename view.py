#!/usr/bin/python

import kwdb
import config

print "Content-type: text/html\n"

if config.path:
    page = int(config.path)
    print kwdb.get_page_content(page),
else:
    print "Status: 404\n"
