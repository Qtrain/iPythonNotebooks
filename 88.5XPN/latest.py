# Adds tracks to a playlist

import pprint
import spotipy
import spotipy.util as util
from bs4 import BeautifulSoup
import urllib2
from collections import namedtuple

url='http://www.xpn.org/playlists/xpn2-playlist'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
sp = spotipy.Spotify()
username = '1232493535'
playlist_id = '3rqRcIjm0NUoTF6ThipeYK'
scope = 'playlist-modify'
token = util.prompt_for_user_token(username, scope, client_id='05c13668e5db496f867fa24cb5c1f12e', client_secret='4ca2d9d6b2c24fee8577861ae5ed4c31', redirect_uri='http://localhost:8888/notebooks/88.5XPN/pyspotify.ipynb')
sp = spotipy.Spotify(auth=token)
sp.trace = False



songs=[]
Song = namedtuple("Song", "artist name album")
for link in soup.find_all("li", class_="song"):
  try:
    song = Song._make(link.text.strip()[4:].split(" - "))
    songs.append(song)
  except TypeError:
    print "skipped"

for song in songs:
    search_str = song.name
    result = sp.search(search_str)
    print result
    results = sp.user_playlist_add_tracks(username, playlist_id, result)
print(results)


    
