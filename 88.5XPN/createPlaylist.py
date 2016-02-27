# create a playlist
# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


username = '1232493535'
playlist_name = 'xpn2'
scope = 'playlist-modify'

token = util.prompt_for_user_token(username, scope, client_id='05c13668e5db496f867fa24cb5c1f12e', client_secret='4ca2d9d6b2c24fee8577861ae5ed4c31', redirect_uri='http://localhost:8888/notebooks/88.5XPN/pyspotify.ipynb')


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)
