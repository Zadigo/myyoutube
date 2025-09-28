from notifications.api import views
from django.urls.conf import re_path
from django.urls import re_path

from notifications import views

app_name = 'notifications'

urlpatterns = [
    re_path(
        r'^profile$',
        views.NotificationProfile.as_view(),
        name='detail'
    ),
    re_path(r'^u/(?P<username>[a-z]+)/get-notifications$',
            views.get_notifications, name='get_notifications'),
    re_path(r'^$', views.NotificationsView.as_view(), name='home')
]
