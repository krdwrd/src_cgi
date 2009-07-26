#!/usr/bin/python

import kwdb
import config

if config.path:
    user = '';
    page = 0;

    try:
        page,user = config.path.split('/')
    except(ValueError):
        page = int(config.path)
        user = config.user

    print "Content-type: text/html\n"
    print kwdb.get_subm_content(page, user),
else:
    print "Status: 404\n"
