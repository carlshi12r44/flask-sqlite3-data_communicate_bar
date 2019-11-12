import sqlite3 as sql
from os import path
ROOT = path.dirname(path.relpath((__file__)))

def create_posts(name, content):
    # making connections
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()


# pull all the posts from the html template
def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    # store all entries in the posts
    posts = cur.fetchall()
    return posts
