from django.urls import re_path

from videos.api import views

app_name = 'videos_api'

urlpatterns = [
    re_path(r'^studio/upload$', views.upload_video),
    re_path(r'^studio/videos$', views.ListUserVideos.as_view()),
    re_path(r'^detail/(?P<video_id>vid_[a-zA-Z0-9]+)$', views.get_video),
    re_path(r'^search$', views.search_videos),
    re_path(r'^viewing-profile', views.ViewingProfile.as_view()),
    re_path(r'^list$', views.get_videos)
]
