import sqlite3 as sqlite

HWDB = '/home/projects/krdwrd/db/harvest.db'
db = sqlite.connect(HWDB, check_same_thread = False)
cursor = db.cursor()

def initdb():
    init = ("""
    CREATE TABLE pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE
    );""","""
    CREATE TABLE attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        page_id INTEGER UNIQUE,
        times INTEGER
    );""","""
    CREATE TABLE harvests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE,
        words INTEGER,
        added REAL DEFAULT CURRENT_TIMESTAMP
    );""",)

    for s in init:
        print s
        cursor.execute(s)

def add_page(url):
    try:
        cursor.execute('INSERT INTO pages (url) VALUES (?)', (url, ))
    except sqlite.Error, e:
        print "SQLite error:", e.args[0], "at URL: ",url
        pass

def close():
    commit()
    db.close()

def commit():
    db.commit()

def del_page(page_id):
    cursor.execute('DELETE FROM pages WHERE id = ?', (page_id,))
        
def next_pages(size):
    #cursor.execute('SELECT pages.id,pages.url FROM pages LEFT OUTER JOIN attempts ON page_id = pages.id ORDER by attempts.times, random() LIMIT 1')
    cursor.execute('SELECT tmp.id,tmp.url FROM (SELECT id,url from pages WHERE id >= ABS(RANDOM() % (SELECT MAX(id) FROM pages)) LIMIT ?) as tmp LEFT OUTER JOIN attempts ON page_id = tmp.id ORDER by attempts.times,random() LIMIT ?', (size*10,size,))
    return cursor.fetchall()

def next_page():
    return next_pages()[0]

def attempt_page(page_id):
    cursor.execute('REPLACE INTO attempts (page_id, times) VALUES (?, IFNULL ((SELECT times FROM attempts WHERE page_id=?)+1, 1) )',  (page_id,page_id,))

def add_harvest(url, words):
    try:
        cursor.execute('INSERT INTO harvests (url,words) VALUES (?,?)', (url, words, ))
    except sqlite.Error, e:
        # this might happen when URL already exists - we don't care
        pass

def changes():
    return db.total_changes
    
if __name__ == '__main__':
    initdb()
