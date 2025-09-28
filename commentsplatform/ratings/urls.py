from django.urls import re_path

from ratings.api import views

app_name = 'ratings'

urlpatterns = [
    re_path(
        r'^(?P<pk>\d+)/rate$',
        views.RateComment.as_view(),
        name='rate'
    )
]
