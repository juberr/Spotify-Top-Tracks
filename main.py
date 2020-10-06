import requests
from urllib.parse import quote
import webbrowser
from http import server

client_id = '571d727cf24f46a2ac2a8dbd5e0bb5c5'
client_secret = 'be654e49ddff49ebb33d55172d1d7a7d'
endpoint = 'https://accounts.spotify.com/authorize'
redirect_uri = 'localhost:8000'
scope = 'user-top-read'

class SpotifyAPI():

    def request_auth(self):
        self.client_id = client_id
        self.clinet_secret = client_secret
        self.endpoint = endpoint
        get_request = f'{endpoint}?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'
        webbrowser.open(get_request)


class Handler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

server = server.HTTPServer(('localhost', 8000),Handler)

test = SpotifyAPI()

test.request_auth()



