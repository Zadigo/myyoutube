from django.urls import re_path

from mychannel.api import views

app_name = 'api_channels'

urlpatterns = [
    re_path(
        r'^(?P<channel_id>ch_[a-zA-Z0-9]+)/search$',
        views.SearchUserChannelAPI.as_view(),
        name='search_channel'
    ),
    re_path(
        r'^(?P<channel_id>ch_[a-zA-Z0-9]+)$',
        views.UserChannelAPI.as_view(),
        name='user_channel'
    ),
    re_path(
        r'^$',
        views.UserChannelsAPI.as_view(),
        name='user_channels'
    )
]
