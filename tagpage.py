#!/usr/bin/python

import config
import cgi
import krdwrd
import tempfile

def savepage(url, html):
    # try mapping the url to a (corpus, page) tuple
    parsed = krdwrd.parseurl(url)

    if not parsed:
        return

    corpus, page = parsed

    # build the target filename
    krdwrd.mkuserdir(corpus, config.username)
    of = krdwrd.tagtarget(corpus, page, config.username)

    # and write the annotated html
    f = file(of, 'w')
    f.write('<html src="%s">' % url)
    f.write(html)
    f.write('</html>')
    f.close()

    return True

fs = cgi.FieldStorage()

html = fs.getfirst("html")
url = fs.getfirst("url")


if html and url:
    if savepage(url, html):
        print "Content-Type: text/plain\n"

# only return upon successful execution
# will result in "not found" otherwise



