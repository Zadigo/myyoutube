from accounts.sites import custom_admin_site
from django.contrib import admin
from mychannel.models import (BlockedChannel, ChannelPlaylist, ChannelTag,
                              UserChannel)


class UserChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_on']
    search_fields = ['name', 'user__username', 'category']
    date_hierarchy = 'created_on'
    readonly_fields = ['reference']
    filter_horizontal = ['tags', 'subscribers']
    fieldsets = [
        [
            'General',
            {
                'fields': ['reference', 'user', 'name', 'description']
            }
        ],
        [
            'Visuals',
            {
                'fields': ['banner']
            }
        ],
        [
            'Classification',
            {
                'fields': ['category', 'tags']
            }
        ],
        [
            'Socials',
            {
                'fields': ['instagram', 'facebook', 'tiktok']
            }
        ],
        [
            'Other',
            {
                'fields': ['is_verified']
            }
        ]
    ]


class ChannelPlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    search_fields = ['name']
    date_hierarchy = 'created_on'


class ChannelTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class BlockedChannelAdmin(admin.ModelAdmin):
    list_display = ['user', 'channel']


custom_admin_site.register(UserChannel, UserChannelAdmin)
custom_admin_site.register(ChannelPlaylist, ChannelPlaylistAdmin)
custom_admin_site.register(ChannelTag, ChannelTagAdmin)
custom_admin_site.register(BlockedChannel, BlockedChannelAdmin)
