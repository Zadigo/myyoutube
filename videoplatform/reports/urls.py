from django.urls import re_path
from django.urls.conf import include, path

from reports import views


app_name = 'reports'

urlpatterns = [
    re_path(r'^$', views.UserReportsView.as_view(), name='list')
]
