from asyncio.windows_events import NULL
import datetime
import time
import config
import scripts.db as db
import scripts.aspen as aspen
import scripts.spotify as spotify

config.create_database()

actual_name_song = db.get_last_song()

while True:
    try:
        actual_song = aspen.get_actual_song()
        name_song = aspen.get_name_song(actual_song).replace("'", "`")
        artist = aspen.get_artist(actual_song).replace("'", "`")
    except:
        name_song = "unknown"
        artist = "unknown"

    if actual_name_song != name_song:
        actual_name_song = name_song

        release_year = 0
        release_month = 0
        release_day = 0
        spotify_href = ''

        if name_song != "unknown" and artist != "unknown":
            try:
                song_info = spotify.get_song_info(name_song, artist)

                if song_info["tracks"]["items"][0]["album"]["release_date_precision"] == "day":
                    date = song_info["tracks"]["items"][0]["album"]["release_date"].split(
                        '-')
                    release_year = date[0]
                    release_month = date[1]
                    release_day = date[2]
                elif song_info["tracks"]["items"][0]["album"]["release_date_precision"] == "month":
                    date = song_info["tracks"]["items"][0]["album"]["release_date"].split(
                        '-')
                    release_year = date[0]
                    release_month = date[1]
                    release_day = 0
                else:
                    release_year = song_info["tracks"]["items"][0]["album"]["release_date"]
                    release_month = 0
                    release_day = 0

                spotify_href = year = song_info["tracks"]["items"][0]["href"]
            except:
                pass

        print(str(datetime.datetime.now()) + " song: " + name_song + " - artist: " + artist + " - year: " +
              str(release_year) + " - month: " + str(release_month) + " - day: " + str(release_day))

        try:
            db.insert_log(name_song, artist, release_year,
                          release_month, release_day, spotify_href)
        except:
            pass

    time.sleep(20)
