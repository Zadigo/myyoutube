from django.contrib import admin

from myadmin.sites import custom_admin
from playlists.models import Playlist


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'visibility', 'created_on']
    search_fields = ['name', 'user__username', 'visibility']
    sortable_by = ['name', 'visibility']
    filter_horizontal = ['videos']
    date_hierarchy = 'created_on'


custom_admin.register(Playlist, PlaylistAdmin)
