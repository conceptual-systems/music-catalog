from abc import ABC
from artist import artist
from album import album
from track import track
from genre import genre
from tag import tag


class Platform(ABC):
	def __init__(self, name):
		self.name = name
	
	self.api_url = None

	# Which of our class types this platform has
	self.models = []


class Spotify(Platform):
	self.name = "Spotify"
	self.api_url = None
	self.models = [artist, album, track, genre]

class LastFm(Platform):
	self.name = "Last FM"
	self.api_url = None
	self.models = [artist, album, track, tag]