import sys, codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

import cgitb
cgitb.enable()

from os import environ, umask
umask(0002)

import kwdb

baseurl = 'https://krdwrd.org/pages/bin'

path = environ.get("PATH_INFO", "/").strip('/')

username = environ.get("REMOTE_USER")
if not username:
    raise Exception("Not logged in")
user = kwdb.get_userid(username)


