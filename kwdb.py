try:
    import sqlite3 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

KWDB = '/tmp/kw.db'

db = sqlite.connect(KWDB)

cursor = db.cursor()

def initdb():
    init = ("""
    CREATE TABLE corpora (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        active INTEGER DEFAULT 1
    );""","""
    CREATE TABLE pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        corpus_id INTEGER,
        url TEXT UNIQUE,
        content TEXT
    );""","""
    CREATE TABLE submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        page_id INTEGER,
        user_id INTEGER,
        content TEXT,
        added REAL DEFAULT CURRENT_TIMESTAMP
    );""","""
    CREATE TABLE annotations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        page_id INTEGER,
        tags TEXT
    );""","""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );""",)

    for s in init:
        cursor.execute(s)

def add_corpus(name):
    cursor.execute('INSERT INTO corpora (name) VALUES (?)', (name,))
    return get_corpus(name)

def get_row(err):
    res = cursor.fetchall()
    if not res:
        raise Exception(err)
    return res[0]

def get_corpus(name):
    cursor.execute('SELECT id FROM corpora WHERE name = ?', (name,))
    return get_row("No such corpus: %s" % name)[0]

def get_corpora():
    cursor.execute('SELECT id, name FROM corpora WHERE active = 1')
    return cursor.fetchall()

def add_page(corpus_id, url, content):
    cursor.execute('INSERT INTO pages (corpus_id, url, content) VALUES (?, ?, ?)', (corpus_id, url, content,))

def get_page(page_id):
    cursor.execute('SELECT * FROM pages WHERE id = ?', (page_id,))
    return get_row("No such page: %s" % page_id)

def get_page_content(page_id):
    cursor.execute('SELECT content FROM pages WHERE id = ?', (page_id,))
    return get_row("No such page: %s" % page_id)[0]

def add_user(name):
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    uid = get_userid(name, False)
    db.commit()
    return uid

def get_userid(name, create=True):
    cursor.execute('SELECT id FROM users WHERE name = ?', (name,))
    res = cursor.fetchall()
    if not res:
        if create:
            return add_user(name)
        else:
            raise Exception("No such user: %s" % name)
    return res[0][0]

def pages_left(corpus_id, user_id):
    cursor.execute('SELECT id FROM pages WHERE corpus_id = ? AND NOT id IN (SELECT page_id FROM submissions WHERE user_id = ?) ORDER BY id', (corpus_id, user_id,))
    return [i[0] for i in cursor.fetchall()]

def count_pages_done(corpus_id, user_id):
    cursor.execute('SELECT COUNT(id) FROM pages WHERE corpus_id = ? AND id IN (SELECT page_id FROM submissions WHERE user_id = ?)', (corpus_id, user_id,))
    return get_row("Error counting pages left")[0]

def pages_done(corpus_id, user_id):
    cursor.execute('SELECT page_id FROM submissions WHERE user_id = ? AND page_id in (SELECT id FROM pages WHERE corpus_id = ?) ORDER BY added', (user_id, corpus_id,))
    return [i[0] for i in cursor.fetchall()]

def count_pages_corpus(corpus_id):
    cursor.execute('SELECT COUNT(id) FROM pages WHERE corpus_id = ?', (corpus_id,))
    return get_row("Error counting corpus pages.")[0]
    
def add_submission(user_id, page_id, content):
    cursor.execute('INSERT INTO submissions (user_id, page_id, content) VALUES (?, ?, ?)', (user_id, page_id, content,))

def get_subm_content(page_id, user_id):
    cursor.execute('SELECT content FROM submissions WHERE page_id = ? AND user_id = ?', (page_id, user_id,))
    return get_row("No such page: %s" % page_id)[0]


def get_annotation(page_id):
    cursor.execute('SELECT tags FROM annotations WHERE page_id = ?', (page_id,))
    return get_row("No annotation for page: %s" % page_id)[0]


if __name__ == '__main__':
    initdb()
