#!/usr/bin/python
import kwdb
import config

corpora = kwdb.get_corpora()

print "Content-type: text/html\n"

print """<html><head><title>My KrdWrd Stats</title>
<link rel="stylesheet" type="text/css" href="../static/krdwrd.css" />
<script type="text/javascript">
function del_page(page)
{
    return confirm("Clear annotation for page " + page + "?");
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
for corpus_id, corpus in corpora:
    all = kwdb.count_pages_corpus(corpus_id)
    done = kwdb.count_pages_done(corpus_id, config.user) 
    left = all - done
    per = 100.0 * done / all
    green = per * 2.55
    red = 255 - per * 2.55
    print """<p><div style="margin-right: 10px; width: 100px; border: 1px solid #000; float: left;">
		        <div style="background-color: rgb(%d, %d, 0); width: %dpx; height: 20px;"></div></div>""" % (red, green, per)
    print """<a href="#%s">%s</a> : """ % (corpus, corpus,)
    print done
    print " of "
    print all
    print " - "
    if left > 0:
        print left
        print " to go. "
    else:
        print "done!"
    print "</p>"
print """</div>"""

for corpus_id, corpus in corpora:
    print """<div class="corpus"><h3><a name="%s"/>%s</h3>""" % (corpus, corpus)
    pages = kwdb.pages_done(corpus_id, config.user)
    if pages:
      print "<ul>"
      for i, page_id in reversed(list(enumerate(pages))):
        fresh = "%s/view/%s\n" % (config.baseurl, page_id, )
        subm = "%s/subm/%s\n" % (config.baseurl, page_id, )
        print """<li> %04d <a href="%s">fresh</a> <a href="%s">my annotation</a> """ % (i, fresh, subm) 
        print """ [<a href="delpage/%d" onclick="return del_page('%s');">del</a>]""" % (page_id, i, )
      print "</ul>"
      print """[ <a href="delcorpus/%d"  onclick="return del_corpus('%s');">delete all annotations</a> ]""" % (corpus_id, corpus,  )
    else:
      print "no annotations"
    print "</div>"

print "</body></html>"
