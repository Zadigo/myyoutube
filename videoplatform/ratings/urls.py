from django.urls import include, re_path
from django.urls.conf import path

from ratings import views

app_name = 'ratings'

videopatterns = [
    re_path(r'^switch$', views.switch_state, name='switch'),
    re_path(r'^remove$', views.remove_like, name='remove'),
    re_path(r'^dislike$', views.dislike_video, name='dislike'),
    re_path(r'^like$', views.like_video, name='like')
]

urlpatterns = [
    path('video/', include((videopatterns, app_name), namespace='rate_video')),

    # re_path(r'^rate-video', views.rate_video, name='video'),
    re_path(r'^rate-comment', views.rate_comment, name='comment'),
    re_path(r'^rate-reply', views.rate_reply, name='reply'),
]
