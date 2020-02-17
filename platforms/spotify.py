import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


class Client:
    def __init__(self):
        self.auth()

    def auth(self):
        self.api = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_user_playlists(self, user):
        return self.api.user_playlists(user)



### Old code below from 2015
def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s") % (i, track['artists'][0]['name'],
            track['name'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)
