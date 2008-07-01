import sys, codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

from os import environ, umask
umask(0002)

import kwerror 
kwerror.enable(logdir="/home/projects/krdwrd/log")

import kwdb

baseurl = 'https://krdwrd.org/pages/bin'

path = environ.get("PATH_INFO", "/").strip('/')

username = environ.get("REMOTE_USER")
if not username:
    raise Exception("Not logged in")
user = kwdb.get_userid(username)


