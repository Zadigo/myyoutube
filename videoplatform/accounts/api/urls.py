from django.urls.conf import re_path

from accounts.api import views

app_name = 'accounts_api'

urlpatterns = [
    re_path(
        r'^notifications$',
        views.UpdateNotifications.as_view()
    ),
    re_path(
        r'^viewing-profile$',
        views.ViewingProfileDetails.as_view(),
        name='viewing_profile'
    ),
    re_path(
        r'^base$',
        views.BaseAccountDetails.as_view(),
        name='account_details'
    )
]
