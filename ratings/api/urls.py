from django.urls import re_path

from ratings.api import views

urlpatterns = [
    re_path(r'^videos/(?P<video_id>vid_[a-zA-Z0-9]+)$', views.rate_video)
]
