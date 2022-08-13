from django.urls import include, re_path
from django.urls import path

from accounts import views, views_profile

app_name = 'accounts'

passwordpatterns = [
    re_path('^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>\w+\-\w+)$',
                views.UnauthenticatedPasswordResetView.as_view(), name='reset'),
    re_path('^forgot-password$', views.ForgotPasswordView.as_view(), name='forgot')
]

profilepatterns = [
    re_path('^change-password$', views_profile.ChangePasswordView.as_view(), name='change_password'),
    re_path('^contact-preferences$', views_profile.ContactPreferencesView.as_view(), name='contact'),
    re_path('^payment-methods$', views_profile.PaymentMethodsView.as_view(), name='payment'),
    re_path('^delete$', views_profile.ProfileDeleteView.as_view(), name='delete'),
    re_path('^data$', views_profile.ProfileDataView.as_view(), name='data'),
    re_path('^information$', views_profile.InformationView.as_view(), name='information'),
    re_path('^$', views_profile.IndexView.as_view(), name='home'),
]

urlpatterns = [
    path('profile/', include((profilepatterns, app_name), namespace='profile')),
    path('password/', include((passwordpatterns, app_name), namespace='password')),

    re_path('^login$', views.LoginView.as_view(), name='login'),
    re_path('^logout$', views.LogoutView.as_view(), name='logout'),
    re_path('^signup$', views.SignupView.as_view(), name='signup'),
]
