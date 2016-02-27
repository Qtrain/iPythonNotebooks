from bs4 import BeautifulSoup
import urllib2
from collections import namedtuple
import spotipy
import sys
import pprint

url='http://www.xpn.org/playlists/xpn2-playlist'
page = urllib2.urlopen(url)


soup = BeautifulSoup(page.read())

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
    
sp = spotipy.Spotify()
result = sp.search(search_str)
pprint.pprint(result)
