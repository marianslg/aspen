import http.client
import re

def get_actual_song():
    conn = http.client.HTTPSConnection("us-b4-p-e-ft6-audio.cdn.mdstrm.com")
    payload = ''
    headers = {}
    conn.request("GET", "/live-audio-aw/60a2745ff943100826374a70/playlist.m3u8?listeningSessionID=61e56819e0a91de6_823614_ze00vc7z__0000002O19J&downloadSessionID=0&aid=60106eadf34de307dd720e7b&dnt=true&uid=DHphDahxfZ9DQIANcIaa0FiZdOIA64il&sid=yjCcuHsRsEFAN0j8deQRuKPumxWUCwle&pid=ThIRC06jwp0jLaZbZcfB5m6smf6Vxwbb&ref=fmaspen.com&es=us-b4-p-e-ft6-audio.cdn.mdstrm.com&ote=1643334201868&ot=O4je0GDbE_BA227sLi5wqA&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&referer=https%253A%252F%252Ffmaspen.com%252F&propertyName=mediastream-player-aspen-pie&propertyType=web-app&propertyVersion=v0.0.183", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
  
def get_name_song(data):
   return re.search('title="(.*)",artist="', data).group(1)

def get_artist(data):
   return re.search(',artist="(.*)"\r\n', data).group(1)