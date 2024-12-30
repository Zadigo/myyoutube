from django.urls import re_path
from videos.api import views

app_name = 'videos_api'

urlpatterns = [
    re_path(
        r'^studio/upload$',
        # views.upload_video,
        views.UploadVideo.as_view(),
        name='studio_upload'
    ),
    re_path(
        r'^studio/videos$',
        views.ListUserVideos.as_view(),
        name='studio_videos'
    ),
    re_path(
        r'^(?P<video_id>vid_[a-zA-Z0-9]+)$',
        views.GetVideo.as_view(),
        name='video'
    ),
    re_path(
        r'^(?P<video_id>vid_[a-zA-Z0-9]+)/comment$',
        views.CreateCommentAPI.as_view(),
        name='create_comment'
    ),
    re_path(
        r'^s/(?P<video_id>vid_[a-zA-Z0-9]+)$',
        views.VideoStreamView.as_view(),
        name='stream'
    ),
    re_path(
        r'^categories/(?P<category>\w+)/sub-categories$',
        views.ListVideoSubcategories.as_view({'get': 'list'})
    ),
    re_path(
        r'^categories$',
        views.ListVideoCategories.as_view({'get': 'list'})
    ),
    re_path(
        r'^search$',
        views.search_videos
    ),
    re_path(
        r'^viewing-profile',
        views.ViewingProfile.as_view()
    ),
    re_path(
        r'^$',
        views.ListVideos.as_view(),
        name='videos'
    )
]
