from django.urls import re_path

from videos import api_views

urlpatterns = [
    re_path(r'^detail/(?P<reference>vid_[a-zA-Z]+)$', api_views.get_video),
    re_path(r'^search$', api_views.search_videos),
    re_path(r'^list$', api_views.get_videos)
]
