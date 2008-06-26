#!/usr/bin/python
import krdwrd
import config
import os

corpora = dict((corpus, krdwrd.get_user_tagged(corpus, config.username)) \
               for corpus in config.corpora)

print "Content-type: text/html\n"

print """<html><head><title>My KrdWrd Stats</title>
<link rel="stylesheet" type="text/css" href="../krdwrd.css" />
<script type="text/javascript">
function del_page(corpus, page)
{
    return confirm("Clear annotation for " + page + " from corpus " + corpus + "?");
}
function del_corpus(corpus)
{
    return confirm("Clear ALL your annotations from corpus " + corpus + "?");
}
</script>
</head>
<body>
"""

print """<div class="corpus"><h2>%s's KrdWrd Stats</h2>""" % config.username
for corpus, pages in corpora.items():
    clen = len(krdwrd.get_pages(corpus))
    plen = pages and len(pages) or 0
    per = clen and int(100.0 * float(plen) / clen) or 0
    green = per * 2.55
    red = 255 - per * 2.55
    print """<p><div style="margin-right: 10px; width: 100px; border: 1px solid #000; float: left;">
		        <div style="background-color: rgb(%d, %d, 0); width: %dpx; height: 20px;"></div></div>""" % (red, green, per)
    print """<a href="#%s">%s</a> : """ % (corpus, corpus,)
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
    print """<div class="corpus"><h3><a name="%s"/>%s</h3>""" % (corpus, corpus)
    if pages:
      print "<ul>"
      for i, page in reversed(list(enumerate(pages))):
        url = krdwrd.usertagurl(corpus, page, config.username)
        print """<li> <a href="%s">%03d</a>""" % (url, i) 
        print """ [<a href="" onclick="return del_page('%s', '%s');">del</a>]""" % (corpus, page)
        img = os.path.splitext(page)[0] + ".png"
        fsi = os.path.join(config.srcdir(corpus), img)
        if os.path.isfile(fsi):
            url = os.path.join(config.srcurl(corpus), img)
            print """ [<a href="%s">img</a>]""" % (url,)
      print "</ul>"
      print """[ <a href=""  onclick="return del_corpus('%s');">delete all annotations</a> ]""" % (corpus,  )
    else:
      print "no annotations"
    print "</div>"

print "</body></html>"
