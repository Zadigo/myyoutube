from mychannel import api_views
from django.urls import re_path

app_name = 'mychannel_api'

urlpatterns = [
    re_path(
        r'^search/(?P<reference>ch_[a-zA-Z0-9]+)$',
        api_views.search_videos_view
    ),
    re_path(
        r'^(?P<reference>ch_[a-zA-Z0-9]+)$',
        api_views.channel_view
    ),
    re_path(
        r'^list$',
        api_views.channels_view
    )
]
