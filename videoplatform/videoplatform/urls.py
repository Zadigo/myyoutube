import debug_toolbar
from accounts.sites import custom_admin_site
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular import views as spectacular_views
from graphene_django.views import GraphQLView
from rest_framework_simplejwt import views as jwt_views

from videoplatform.views import ViewingProfileToken

urlpatterns = [
    path(
        'graphql/', 
         GraphQLView.as_view(graphiql=True)
    ),
    path(
        '__debug__/', 
        include(debug_toolbar.urls)
    ),
    re_path(
        r'^v1/viewing/id$',
        ViewingProfileToken.as_view(),
        name='viewing_profile_id'
    ),
    path(
        'v1/notifications/',
        include('notifications.api.urls')
    ),
    path(
        'v1/playlists/',
        include('playlists.api.urls')
    ),
    path(
        'v1/ratings/',
        include('ratings.api.urls')
    ),
    path(
        'v1/comments/',
        include('comments.api.urls')
    ),
    path(
        'v1/accounts/',
        include('accounts.api.urls')
    ),
    path(
        'v1/user-channels/',
        include('mychannel.api.urls')
    ),
    path(
        'v1/videos/',
        include('videos.api.urls')
    ),
    path(
        'auth/v1/token/verify/',
        jwt_views.TokenVerifyView.as_view(),
        name='token_verify'
    ),
    path(
        'auth/v1/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'auth/v1/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/schema/',
        spectacular_views.SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/schema/swagger-ui/',
        spectacular_views.SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        spectacular_views.SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path(
        'api/rest/',
        include('rest_framework.urls'),
        name='rest_framework'
    ),
    path('admin/secondary/', custom_admin_site.urls),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
