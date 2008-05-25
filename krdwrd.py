import config
import os

def get_pages(corpus):
    if corpus and corpus in config.corpora:
        return os.listdir(config.srcdir(corpus))

def get_user_tagged(corpus, user):
    if corpus and corpus in config.corpora:
        userd = userdir(corpus, user)
        if os.path.isdir(userd):
            return os.listdir(userd)

def parseurl(url):
    components = url.split('/')
    page = os.path.splitext(components[-1])[0]
    corpus = components[-3]
    if corpus in config.corpora:
        return (corpus, page)

def userdir(corpus, username):
    return os.path.join(config.basedir, 'dat', corpus, 'tagged', username)

def mkuserdir(corpus, username):
    ud = userdir(corpus, username)
    if not os.path.isdir(ud):
        os.mkdir(ud)

def tagtarget(corpus, page, username):
    return os.path.join(userdir(corpus, username), '%s.html' % (page))




