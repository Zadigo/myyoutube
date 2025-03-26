from django.urls import re_path
from videos.api import views

app_name = 'videos_api'

urlpatterns = [
    re_path(
        r'^feed-builder$',
        views.FeedBuilderEndpoint.as_view(),
        name='feed_builder_videos'
    ),
    re_path(
        r'^studio/upload$',
        views.UploadVideo.as_view(),
        name='upload_video'
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
        views.ListVideoSubcategories.as_view({'get': 'list'}),
        name='sub_categories'
    ),
    re_path(
        r'^categories$',
        views.ListVideoCategories.as_view({'get': 'list'}),
        name='categories'
    ),
    re_path(
        r'^search$',
        views.search_videos,
        name='search'
    ),
    re_path(
        r'^viewing-profile',
        views.ViewingProfile.as_view(),
        name='viewing_profile'
    ),
    re_path(
        r'^$',
        views.ListVideos.as_view(),
        name='videos'
    )
]
