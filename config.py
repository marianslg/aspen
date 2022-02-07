import sqlite3

def create_database():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS log_songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        name_song TEXT NULL,
        artist TEXT NULL,
        release_year INTEGER NULL,
        release_month INTEGER NULL,
        release_day INTEGER NULL,
        spotify_href TEXT NULL
        );''')
    con.commit()
    con.close()