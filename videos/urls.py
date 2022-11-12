from django.urls import re_path
from django.urls.conf import include, path

from videos import views
from videos._views import feed, playlist, api

app_name = 'videos'


playlisturls = [
    re_path(r'^add-remove$', views.add_or_remove_video_in_playlist, name='add_remove_video'),
    re_path(r'^new-playlist$', views.new_playlist, name='new'),
    re_path(r'(?P<pk>\d+)', views.PlaylistView.as_view(), name='detail')
]


urlpatterns = [
    path('playlist/', include((playlisturls, app_name), namespace='playlists')),
    
    re_path(r'^(?P<reference>[a-z0-9]+)/view$', api.add_view_count, name='count_view'),

    re_path(r'^(?P<reference>[a-z0-9]+)$', feed.VideoView.as_view(), name='detail'),
    re_path(r'^search$', feed.SearchView.as_view(), name='search'),
    re_path(r'^$', feed.FeedView.as_view(), name='feed'),
]
