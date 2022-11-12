from django.urls import include, re_path
from django.urls import path

from accounts import views, views_profile

app_name = 'accounts'

# passwordpatterns = [
#     re_path('^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>\w+\-\w+)$', views.UnauthenticatedPasswordResetView.as_view(), name='reset'),
#     re_path('^forgot-password$', views.ForgotPasswordView.as_view(), name='forgot')
# ]

# profilepatterns = [
#     re_path(r'^change-password$', views_profile.ChangePasswordView.as_view(), name='change_password'),
#     re_path(r'^contact-preferences$', views_profile.ContactPreferencesView.as_view(), name='contact'),
#     re_path(r'^payment-methods$', views_profile.PaymentMethodsView.as_view(), name='payment'),
#     re_path(r'^delete$', views_profile.ProfileDeleteView.as_view(), name='delete'),
#     re_path(r'^data$', views_profile.ProfileDataView.as_view(), name='data'),
#     re_path(r'^information$', views_profile.InformationView.as_view(), name='information'),
#     re_path(r'^$', views_profile.IndexView.as_view(), name='home'),
# ]

urlpatterns = [
    # path('profile/', include((profilepatterns, app_name), namespace='profile')),
    # path('password/', include((passwordpatterns, app_name), namespace='password')),

    re_path(r'^forgot-password-reset/(?P<uidb64>\w+)/(?P<token>[a-z0-9-]+)$',
            views.ForgotPasswordResetView.as_view(), name='forgot_password_reset'),
    re_path(r'^forgot-password$',
            views.ForgotPasswordView.as_view(), name='forgot_password'),
    re_path(r'^activate/(?P<token>[a-zA-Z0-9]+)$', 
            views.ActivateAccountView.as_view(), name='activate'),
    re_path(r'^login$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup$', views.SignupView.as_view(), name='signup'),
]
