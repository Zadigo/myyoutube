from django.urls import include, re_path
from django.urls.conf import path

from school import views

app_name = 'school'

videopatterns = [
    re_path(r'^first-video$', views.GettingStartedView.as_view(), name='first-video')
]

urlpatterns = [
    path('editing/', include((videopatterns, app_name), namespace='editing')),
    re_path(r'^getting-started$', views.GettingStartedView.as_view(), name='starting')
]
