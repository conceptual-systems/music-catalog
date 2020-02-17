from . import playlist

class User:
	def __init__(self, name):
		self.name = name

		self.id_ = None
		self.playlists = []

	def get_playlists(self, platform):
		self.playlists = platform.get_user_playlists(self.id_)
		return self.playlists