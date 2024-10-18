from django.urls.conf import re_path

from comments.api import views

app_name = 'api_comments'

urlpatterns = [
    re_path(
        r'^(?P<pk>\d+)/reply$',
        views.CreateReplyAPI.as_view(),
        name='created_reply'
    ),
    re_path(
        r'^(?P<video_id>vid\_[a-zA-Z0-9]+)$',
        views.CommentAPI.as_view(),
        name='comments'
    )
]
