#!/usr/bin/python
import kwdb
import config

corpora = kwdb.get_corpora()
min_user_id = 5

print "Content-type: text/html\n"

print """<html><head><title>KrdWrd Stats</title>
<link rel="stylesheet" type="text/css" href="../static/krdwrd.css" />
</head>
<body>
"""

print """<div class="corpus"><img src="../static/krdwrd.png" /><span class="head">KrdWrd Stats</h2></span><br/>"""
print """<table class="stats_table">"""
print """<tr><th></th><th>pages</th><th>subs</th><th>users</th><th>&#248; subs/page</th></tr>"""
for corpus_id, corpus in corpora:
    all = kwdb.count_pages_corpus(corpus_id)
    submissions = kwdb.count_pages_done_incorpus(corpus_id, min_user_id) 
    users = kwdb.count_users_incorpus(corpus_id, min_user_id)
    if users > 0:
        subs_per_page = round(float(submissions) / all, 2)
    else:
        subs_per_page = 0

    print """<tr><td>"""
    print """<a href="#%s">%s</a> """ % (corpus, corpus,)
    print """</td><td align="right">"""
    print all
    print """</td><td align="right">"""
    print submissions 
    print """</td><td align="right">"""
    print users
    print """</td><td align="right">"""
    print subs_per_page
    print "</td></tr>"
print """</table></div>"""

for corpus_id, corpus in corpora:
    print """<div class="corpus"><a name="%s"></a><span class="shead">%s</span>""" % (corpus, corpus)
    pages = kwdb.pages_incorpus(corpus_id)
    pages_done_user = [i[0] for i in kwdb.pages_done(corpus_id, config.user)] 
    pages_done = kwdb.pages_done_incorpus(corpus_id)
    submissions_dict = {} 

    for k,v in pages_done:
        submissions_dict.setdefault(k, []).append(v)

    if pages:
        print """<br/>"""
        print """<table>"""

        for id, url in pages:
            fresh = "%s/view/%s\n" % (config.baseurl, id, )
    	    print """<tr><td>%04d</td><td style="white-space: nowrap;"><a href="%s">original</a> """ % (id, fresh) 

            if id in pages_done_user:
                mine = "%s/subm/%s\n" % (config.baseurl, id, )
                print """<a href="%s">mine</a>""" % (mine) 
            else:
                print """-"""

            print """ <a href="%s">URL</a> |""" % (url) 

            try:
                submissions = submissions_dict[id]
                merged = "%s/dat/%s/merged/%s" % (config.baseurl[:-4], corpus, id)
                print """ <a href="%s">merged</a> (%d):</td></tr> """ % (merged, len(submissions))

                print """<tr><td><td /><table><tr>"""
                tmp = 0
                for dict_id in submissions_dict[id]:
                    tmp += 1
                    submits = "%s/subm/%s/%s" % (config.baseurl, id, dict_id) 
                    if (tmp == 15): 
                        print """<td>...</td>"""
                    elif (tmp > 15): 
                        continue
                    else:
                        print """<td align="right"><a href="%s">%3d</a></td>""" % (submits, dict_id) 
            except KeyError:
                print """</td></tr><tr><td><td /><table><tr>"""

            print """</tr></table></td></tr>"""

        print """</table>"""

    else:
        print "<br/>no pages to show"

    print "</div>"

print "</body></html>"
