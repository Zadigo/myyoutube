from django.urls import re_path
from playlists.api import views

app_name = 'playlists_api'

urlpatterns = [
    re_path(
        r'^(?P<playlist_id>ply\_[a-zA-Z0-9]+)/add$',
        views.AddToPlaylist.as_view(),
        name='add_video'
    ),
    re_path(
        r'^create$',
        views.CreatePlaylist.as_view(),
        name='create'
    ),
    re_path(
        r'^$',
        views.ListPlaylists.as_view(),
        name='list'
    )
]
