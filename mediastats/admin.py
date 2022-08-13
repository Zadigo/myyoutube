from django.contrib import admin
from mediastats.models import MediaView


@admin.register(MediaView)
class MediaViewAdmin(admin.ModelAdmin):
    list_display = ['reference', 'get_media_type', 'duration']
    search_fields = ['video__name']
    date_hierarchy = 'created_on'
