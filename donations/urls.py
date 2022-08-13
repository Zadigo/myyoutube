
from donations.views import cancel_donation
from django.urls import re_path

from donations import views

app_name = 'donations'

urlpatterns = [
    re_path(r'^cancel$', views.cancel_donation, name='cancel'),
    re_path(r'^send$', views.send_donation, name='send')
]
