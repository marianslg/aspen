import datetime
import sqlite3


def insert_log(name_song, artist, release_year, release_month, release_day, spotify_href):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO log_songs (date, name_song, artist, release_year, release_month, release_day, spotify_href) " +
                "VALUES ('"+str(datetime.datetime.now())+"', '"+name_song+"','" + artist+"',"+str(release_year)+","+str(release_month)+","+str(release_day)+",'"+spotify_href+"')")
    con.commit()
    con.close()


def get_last_song():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM log_songs ORDER BY id DESC LIMIT 1')
    res = cur.fetchone()
    if res != None:
        return res[2]
    else:
        return ""
