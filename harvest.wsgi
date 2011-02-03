import sys
sys.path.append('/home/projects/krdwrd/trunk/src/cgi')
import harvestdb as hwdb

import mutex
mu = mutex.mutex()

from collections import deque
pages = deque() 
attempts = deque()
harvests = deque()
batchsize = 2500

def application(environ, start_response):
    global pages,attempts,harvests,batchsize

    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']

    if path == '/next' and method == 'GET':
        page_id, url = get_page()
        put_attempt(int(page_id))

        start_response('200 OK', [('content-type', 'text/plain; charset=utf-8')])
        output=(str(page_id)+"\n"+url).encode('utf-8')
        return [output]

    elif path == '/success' and method == 'POST':
        import cgi
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        page_id = post.getfirst("page_id")
        url = post.getfirst("url")
        words = post.getfirst("words")

        put_harvest(page_id,url,words)

        start_response('201 OK', [])
        return [] 

    elif path == '/info' and method == 'GET':
        start_response('200 OK', [('content-type', 'text/plain')])
        return ("bs:"+str(batchsize)+", atmpts:"+str(len(attempts))+", hrvsts:"+str(len(harvests))+", pgs:"+str(len(pages))+"\n")
        # +str([str(i)+":"+str(j) for i,j in pages]))

    elif path == '/commit' and method == 'GET':
        hwdb.commit()
        start_response('200 OK', [('content-type', 'text/plain')])
        return []

    start_response('404 NOT FOUND', [('content-type', 'text/plain')])
    return ('Not Found',)

def get_next_pages():
    global pages,batchsize
    pages = hwdb.next_pages(batchsize)

def get_page():
    global mu,pages,attempts,harvests,batchsize
    try:
        while mu.locked:
            import time
            time.sleep(5)
        return pages.pop()
    except IndexError:
        if mu.testandset():
            try:
                put_attempts()
                put_harvests()
                hwdb.commit()
                get_next_pages()
                return pages.pop()
            finally:
                mu.unlock()
        else:
            # this is not so good...
            return get_page()
            
def put_attempt(page_id):
    global attempts
    attempts.append(page_id)

def put_attempts():
    global attempts
    while attempts:
        hwdb.attempt_page(attempts.pop())

def put_harvest(page_id,url,words):
    global harvests
    harvests.append([page_id,url,words])

def put_harvests():
    global harvests
    while harvests:
        page_id,url,words = harvests.pop()
        hwdb.add_harvest(url,words)
        hwdb.del_page(page_id) 
    
# vim: filetype=python
