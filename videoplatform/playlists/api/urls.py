from django.urls import re_path

from playlists.api import views

app_name = 'playlists_api'

urlpatterns = [
    re_path(r'^(?P<playlist_id>ply\_[a-zA-Z0-9]+)/add$', views.AddToPlaylist.as_view()),
    re_path(r'^create$', views.CreatePlaylist.as_view()),
    re_path(r'^$', views.ListPlaylists.as_view())
]
