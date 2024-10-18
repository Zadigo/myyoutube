from django.urls import re_path

from notifications import views

app_name = 'notifications'

urlpatterns = [
    re_path(r'^u/(?P<username>[a-z]+)/get-notifications$', views.get_notifications, name='get_notifications'),
    re_path(r'^$', views.NotificationsView.as_view(), name='home')
]
