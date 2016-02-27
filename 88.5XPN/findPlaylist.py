import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util


username = '1232493535' 
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope, client_id='05c13668e5db496f867fa24cb5c1f12e', client_secret='4ca2d9d6b2c24fee8577861ae5ed4c31', redirect_uri='http://localhost:8888/notebooks/88.5XPN/pyspotify.ipynb')

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
       print(playlist['name'])
       print(playlist['id'])
else:
    print("Can't get token for", username)
