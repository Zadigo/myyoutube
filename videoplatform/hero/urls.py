from django.urls import re_path

from hero import views

app_name = 'hero'

urlpatterns = [
    re_path(r'^send-message$', views.send_message, name='contact'),
    re_path(r'^$', views.HeroView.as_view(), name='home')
]
