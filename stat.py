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

print """<div class="corpus"><img src="../static/krdwrd.png" /><span class="head">%s's KrdWrd Stats</h2></span><br/>""" % config.username
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
    print """<div class="corpus"><a name="%s"></a><span class="shead">%s</span>""" % (corpus, corpus)
    pages = kwdb.pages_done(corpus_id, config.user)
    if pages:
      print """(<a href="delcorpus/%d"  onclick="return del_corpus('%s');">delete all</a>) <br/>""" % (corpus_id, corpus,  )
      print "<ul>"
      while len(pages) > 0:
        page_id, added = pages.pop()
        submits = 1
        while len(pages) > 0 and pages[len(pages)-1][0] == page_id: 
          submits += 1
          pages.pop()
        fresh = "%s/view/%s\n" % (config.baseurl, page_id, )
        subm = "%s/subm/%s\n" % (config.baseurl, page_id, )
        print """<li> %04d %s <a href="%s">original</a> <a href="%s/%s">mine/%s</a> """ % (page_id, added, fresh, subm, config.user, submits) 
        print """ (<a href="delpage/%d" onclick="return del_page('%s');">delete</a>)""" % (page_id, page_id, )
      print "</ul>"
    else:
      print "<br/>no annotations"
    print "</div>"

print "</body></html>"
