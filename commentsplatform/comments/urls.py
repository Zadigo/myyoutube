from django.urls import re_path

from comments import views

app_name = 'comments'

urlpatterns = [
    re_path(r'^reply$', views.new_reply, name='reply'),
    re_path(r'^new$', views.new_comment, name='new'),

    re_path(r'^$', views.CommentsView.as_view(), name='list')
]
