#!/usr/bin/python

import kwdb
import config

if config.path:
    page = int(config.path)
    mime = kwdb.get_page_mime;
    print """Content-type: %s\n""" % (mime) 
    print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
"""
    print kwdb.get_page_content(page),
    print """</html>"""
else:
    print "Status: 404\n"
