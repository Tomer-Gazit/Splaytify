import requests
from pprint import pprint

token = open('d:\Projects\Splaytify\.token', 'r').read()

headers = {
'Authorization': 'Bearer '+token,
}
response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
resp_json = response.json()

track_id = resp_json['item']['id']
track_name = resp_json['item']['name']
artists = resp_json['item']['artists']
artists_names = ', '.join(
    [artist['name'] for artist in artists]
)
track_cover = resp_json['item']['album']['images'][0]['url']

current_track_info = {
    "id": track_id,
    "name": track_name,
    "artists": artists_names,
    "cover": track_cover
}

pprint(current_track_info, indent=4)