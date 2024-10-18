from accounts.sites import custom_admin_site
from django.contrib import admin

from mychannel.models import ChannelTag, UserChannel, ChannelPlaylist


# @admin.register(UserChannel)
class UserChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_on']
    search_fields = ['name', 'user__username', 'category']
    date_hierarchy = 'created_on'
    readonly_fields = ['reference']
    filter_horizontal = ['tags', 'subscribers']
    fieldsets = [
        ['General', {'fields': ['reference', 'user', 'name', 'description']}],
        ['Visuals', {'fields': ['banner']}],
        ['Classification', {'fields': ['category', 'tags']}],
        ['Socials', {'fields': ['instagram', 'facebook', 'tiktok']}],
        ['Other', {'fields': ['is_verified']}]
    ]


# @admin.register(ChannelPlaylist)
class ChannelPlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    search_fields = ['name']
    date_hierarchy = 'created_on'


# @admin.register(ChannelTag)
class ChannelTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


custom_admin_site.register(UserChannel, UserChannelAdmin)
custom_admin_site.register(ChannelPlaylist, ChannelPlaylistAdmin)
custom_admin_site.register(ChannelTag, ChannelTagAdmin)
