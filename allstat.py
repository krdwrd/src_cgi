#!/usr/bin/python
import kwdb
import config

corpora = kwdb.get_corpora()

print "Content-type: text/html\n"

print """<html><head><title>KrdWrd Stats</title>
<link rel="stylesheet" type="text/css" href="../static/krdwrd.css" />
</head>
<body>
"""

print """<div class="corpus"><img src="../static/krdwrd.png" /><span class="head">KrdWrd Stats</h2></span><br/>"""
print """<table class="stats_table">"""
print """<tr><th></th><th>subs</th><th>users</th><th>pages</th><th>&#248; subs/user</th></tr>"""
for corpus_id, corpus in corpora:
    all = kwdb.count_pages_corpus(corpus_id)
    submissions = kwdb.count_pages_done_incorpus(corpus_id) 
    users = kwdb.count_users_incorpus(corpus_id)
    subs_per_user = int(submissions / users)
    print """<tr><td>"""
    print """<a href="#%s">%s</a> : """ % (corpus, corpus,)
    print """</td><td align="right">"""
    print submissions 
    print """</td><td align="right">"""
    print users
    print """</td><td align="right">"""
    print all
    print """</td><td align="right">"""
    print subs_per_user 
    print "</td></tr>"
print """</table></div>"""

for corpus_id, corpus in corpora:
    print """<div class="corpus"><a name="%s"></a><span class="shead">%s</span>""" % (corpus, corpus)
    pages = kwdb.pages_incorpus(corpus_id)
    pages_done_per_user = [i[0] for i in kwdb.pages_done(corpus_id, config.user)] 
    pages_done = [i[0] for i in kwdb.pages_done_incorpus(corpus_id)]

    if pages:
      print """<br/>"""
      print "<ul>"

      for id, url in reversed(pages):
        fresh = "%s/view/%s\n" % (config.baseurl, id, )
	print """<li> %04d <a href="%s">original</a> """ % (id, fresh) 

        if id in pages_done_per_user:
          mine = "%s/subm/%s\n" % (config.baseurl, id, )
          print """<a href="%s">mine</a>""" % (mine) 
        else:
          print """-"""

        if id in pages_done:
          merge = "%s/merge/%s\n" % (config.baseurl, id, )
          print """<a href="%s">merged</a>""" % (merge) 
        else:
          print """-"""

	print """ | <a href="%s">URL</a> """ % (url) 
      print "</ul>"
    else:
      print "<br/>no annotations"

    print "</div>"

print "</body></html>"
