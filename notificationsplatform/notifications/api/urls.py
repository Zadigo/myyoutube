from django.urls.conf import re_path

from notifications.api import views

app_name = 'notifications_api'

urlpatterns = [
    re_path(
        r'^profile$',
        views.NotificationProfile.as_view(),
        name='detail'
    )
]
