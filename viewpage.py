#!/usr/bin/python

import kwdb
import config

if config.path:
    page = int(config.path)
    mime = kwdb.get_page_mime;
    print """Content-type: %s\n""" % (mime) 
    print kwdb.get_page_content(page),
else:
    print "Status: 404\n"
