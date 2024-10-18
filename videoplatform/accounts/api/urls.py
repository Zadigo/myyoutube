from django.urls.conf import re_path

from accounts.api import views

app_name = 'accounts_api'

urlpatterns = [
    re_path(r'^notifications$', views.UpdateNotifications.as_view()),
    re_path(r'^accounts/base$', views.UpdateNotifications.as_view())
]
