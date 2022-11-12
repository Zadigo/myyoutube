import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from myadmin.sites import custom_admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    
    path('accounts/', include('accounts.urls')),
    path('reports/', include('reports.urls')),
    path('donations/', include('donations.urls')),
    path('academy/', include('school.urls')),
    path('channels/', include('mychannel.urls')),
    path('comments/', include('comments.urls')),
    path('ratings/', include('ratings.urls')),
    path('history/', include('history.urls')),
    path('videos/', include('videos.urls')),
    path('', include('hero.urls')),

    path('admin/', custom_admin.urls),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
