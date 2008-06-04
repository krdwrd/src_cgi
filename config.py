import cgitb
cgitb.enable()

import os.path as osp
from os import environ, umask

umask(0002)

username = environ.get("REMOTE_USER", '')

baseurl = 'https://krdwrd.org/pages/'

basedir = '/srv/www/projects/krdwrd/pages/'

corpora = ['test', 'ggaze', 'ceval']

def srcdir(corpus):
    return osp.join(basedir, 'dat', corpus, 'input')

def tagdir(corpus):
    return osp.join(basedir, 'dat', corpus, 'tagged')

def srcurl(corpus):
    return osp.join(baseurl, 'dat', corpus, 'input')

def tagurl(corpus):
    return osp.join(baseurl, 'dat', corpus, 'tagged')

