from django.urls.conf import re_path

from comments.api import views

app_name = 'comments_api'

urlpatterns = [
    re_path(
        r'^(?P<pk>\d+)/reply$',
        views.CreateReply.as_view(),
        name='reply'
    ),
    re_path(
        r'^(?P<video_id>vid\_[a-zA-Z0-9]+)$',
        views.ListComments.as_view(),
        name='list_comments'
    )
]
