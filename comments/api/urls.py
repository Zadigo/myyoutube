from django.urls.conf import re_path

from comments.api import views

app_name = 'api_comments'

urlpatterns = [
    # re_path(r'^(?P<video_id>vid\_[a-zA-Z0-9]+)/create$', views.create_),
    re_path(r'^(?P<video_id>vid\_[a-zA-Z0-9]+)/create$', views.create_comment),
    re_path(r'^(?P<video_id>vid\_[a-zA-Z0-9]+)$', views.list_comments)
]
