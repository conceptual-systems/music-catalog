from abc import ABC, abstractmethod

class findable(ABC):
	@abstractmethod
	def find_in_platform(platform_name):
		pass


class Artist(findable):
	def __init__(self, **e):
		self.name = e.get('name')

		# lists of Catalog types
		self.tracks = []
		self.albums = []

	def find_in_platform(platform_name):
		pass


class spotify_artist:
	def __init__(self, **e):
		self.id_ = e.get("id")

		self.uri
		self.followers
		self.genres
		self.popularity



# Example usage
def example():
	
	artist("Luke Eargoggle").find_in_platform("Spotify")