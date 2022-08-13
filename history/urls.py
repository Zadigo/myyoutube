from django.urls import re_path
from history import views

app_name = 'history'

urlpatterns = [
    re_path(r'^delete-from-history', views.delete_from_history, name='delete-from-history'),
    re_path(r'^delete', views.delete_history, name='delete'),
    re_path(r'^pause', views.pause_history, name='pause'),

    re_path(r'^library', views.MyHistory.as_view(), name='home')
]
