#!/usr/bin/python
import krdwrd
import config

print "Content-type: text/html\n"

print "<html><head><title>My KrdWrd Stats</title></head><body>"

print "<h2>%s's KrdWrd Stats</h2>" % config.username

for corpus in config.corpora:
    print "<h3>Corpus: ", corpus, "</h3>"
    pages = krdwrd.get_user_tagged(corpus, config.username)
    if pages:
      print "<ul>"
      for i, page in reversed(list(enumerate(pages))):
        url = krdwrd.usertagurl(corpus, page, config.username)
        print """<li> <a href="%s">%03d</a>""" % (url, i) 
      print "</ul>"
    else:
      print "no annotations"


print "</body></html>"
