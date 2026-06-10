from django.urls import re_path

from ratings.api import views

app_name = 'ratings_api'

urlpatterns = [
    re_path(
        r'^videos/(?P<video_id>vid_[a-zA-Z0-9]+)$', 
        views.RateVideo.as_view(),
        name='rate_video'
    )
]
