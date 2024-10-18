from accounts.sites import custom_admin_site
from django.contrib import admin
from mediastats.models import MediaView


# @admin.register(MediaView)
class MediaViewAdmin(admin.ModelAdmin):
    list_display = ['reference', 'get_media_type', 'duration']
    search_fields = ['video__name']
    date_hierarchy = 'created_on'
    readonly_fields = ['reference']


custom_admin_site.register(MediaView, MediaViewAdmin)
