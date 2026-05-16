from django.urls import re_path
from django.urls.conf import re_path
from notifications.api import views

app_name = 'notifications'

urlpatterns = [
    re_path(
        r'^profile$',
        views.NotificationProfile.as_view(),
        name='profile'
    ),
    re_path(
        r'^create$',
        views.CreateNotification.as_view(),
        name='create'
    ),
    re_path(
        r'^$',
        views.ListNotifications.as_view(),
        name='list'
    )
]
