from models import user, artist, album, track, label, genre
from platforms import spotify

spotify_client = spotify.Client()

# Top historical

def top_artists(time_interval, time_span):
	pass

def top_genres(time_interval, time_span):
	pass

def top_albums(time_inveral, time_span):
	pass

def top_labels(time_interval, time_span):

	labels = [album.label for album in top_played_albums(time_interval, time_span)]

def top_tags(time_interval, time_span):
	pass

def top_genres(time_interval, time_span):
	pass


# Playlists
def get_user_playlists(user):
	playlists = user.get_playlists(spotify_client)
	return playlists

def top_playlist_tags():
	pass

def top_playlist_genres():
	pass

def export_playlists(user_name):
	pass


# Tracks

def matching_bpm_tracks(track):
	pass

def matching_rhythm_tracks(track):
	matching_bpm_tracks(track)
	pass

# Labels

def find_label_albums(label_name):

	pass

