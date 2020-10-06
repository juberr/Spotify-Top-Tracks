import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import requests
from datetime import date
import secrets


def make_monthly_playlist():
    todays_date = date.today()
    current_month = todays_date.month
    months_reference = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    current_month_name = months_reference[current_month]

    scope = 'user-top-read playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.client_id,
                                                   client_secret=secrets.client_secret,
                                                   scope=scope,
                                                   redirect_uri='http://127.0.0.1:9090'))

    results = sp.current_user_top_tracks(limit=50, time_range='medium_term')
    user = sp.current_user()

    ret = sp.user_playlist_create(user['id'], f'{current_month_name} 2020 Top Tunes', False, False,
                                  f'50 of your most listened to songs in {current_month_name}')

    real_playlist_name = ret['id']

    func_list = []
    for i in results['items']:
        current_track = i['uri']
        func_list += [current_track]

    sp.playlist_add_items(real_playlist_name, func_list)
