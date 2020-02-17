from models import user
from views import views

Me = user.User()

print( views.get_user_playlists(Me) )

