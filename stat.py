#!/usr/bin/python
import krdwrd
import config

corpora = dict((corpus, krdwrd.get_user_tagged(corpus, config.username)) \
               for corpus in config.corpora)

print "Content-type: text/html\n"

print """<html><head><title>My KrdWrd Stats</title>
<link rel="stylesheet" type="text/css" href="../krdwrd.css" />
</head><body>"""

print """<div class="corpus"><h2>%s's KrdWrd Stats</h2>""" % config.username
for corpus, pages in corpora.items():
    clen = len(krdwrd.get_pages(corpus))
    plen = pages and len(pages) or 0
    print """<p><a href="#%s">%s</a> : """ % (corpus, corpus,)
    print plen
    print " of "
    print clen
    print " - "
    if clen > plen:
        print clen - plen
        print " to go. "
    else:
        print "done!"
    print "</p>"
print """</div>"""

for corpus, pages in corpora.items():
    print """<div class="corpus"><h3><a name="%s" />%s</h3>""" % (corpus, corpus,)
    if pages:
      print "<ul>"
      for i, page in reversed(list(enumerate(pages))):
        url = krdwrd.usertagurl(corpus, page, config.username)
        print """<li> <a href="%s">%03d</a>""" % (url, i) 
      print "</ul>"
    else:
      print "no annotations"
    print "</div>"

print "</body></html>"
