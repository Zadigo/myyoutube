from django.contrib import admin
from accounts.sites import custom_admin_site
from playlists.models import Playlist


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'visibility', 'created_on']
    search_fields = ['name', 'user__username', 'visibility']
    sortable_by = ['name', 'visibility']
    filter_horizontal = ['videos']
    date_hierarchy = 'created_on'


custom_admin_site.register(Playlist, PlaylistAdmin)
