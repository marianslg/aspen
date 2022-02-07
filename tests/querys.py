import sqlite3
import threading
import time

con = sqlite3.connect('data.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM log_songs'):
    print(row)
con.close()


con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('SELECT * FROM log_songs ORDER BY id DESC LIMIT 1')
res = cur.fetchone()
if res != None:
    print(res[3])
con.close()
