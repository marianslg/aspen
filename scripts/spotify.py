import http.client
import json
from urllib.parse import urlparse
import config_file
import urllib


def get_song_info(name_song, artist):
    conn = http.client.HTTPSConnection("api.spotify.com")
    payload = ''
    headers = {
        'Authorization': 'Bearer ' + get_access_token()
    }
    params = urllib.parse.urlencode(
        {"q": name_song+" "+artist, "type": "track"})
    conn.request("GET", "/v1/search?" + params, payload, headers)
    coso = conn.getresponse().read().decode("utf-8")
    return json.loads(coso)


def get_access_token():
    conn = http.client.HTTPSConnection("accounts.spotify.com")
    payload = 'grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
        'Authorization': 'Basic  ' + config_file.basic_security
    }
    conn.request("POST", "/api/token", payload, headers)
    return json.loads(conn.getresponse().read().decode("utf-8"))["access_token"]
