from django.urls import re_path, include
from django.urls import path, re_path

from mychannel import views

app_name = 'mychannel'

channelsettings = [
    re_path(r'^delete', views.delete, name='delete'),
    re_path(r'^upload$', views.UploadVideoView.as_view(), name='upload'),
    re_path(r'^customize', views.CustomizeChannelView.as_view(), name='customize'),
    re_path(r'^video/(?P<video_reference>[a-z0-9]+)/edit',
            views.EditVideoView.as_view(), name='video'),
    re_path(r'^videos$', views.ChannelVideosView.as_view(), name='videos'),
]

urlpatterns = [
    re_path(r'^(?P<reference>ch_[a-zA-Z]+)/',
            include((channelsettings, app_name), namespace='settings')),

    re_path(r'^new$', views.create_new_channel, name='new'),

    re_path(r'^(?P<reference>[a-z0-9]+)/subscribe',
            views.subscribe, name='subscribe'),
    re_path(r'^(?P<reference>[a-z0-9]+)/unsubscribe',
            views.unsubscribe, name='unsubscribe'),

    re_path(
        r'^(?P<reference>ch_[a-zA-Z]+)$',
        views.ChannelView.as_view(),
        name='detail'
    ),
    re_path(r'^$', views.ChannelsView.as_view(), name='channels')
]
