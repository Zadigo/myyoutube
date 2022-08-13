from django.contrib import admin

from mychannel.models import ChannelTag, UserChannel, ChannelPlaylist


@admin.register(UserChannel)
class UserChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_on']
    search_fields = ['name', 'user__username', 'category']
    date_hierarchy = 'created_on'
    filter_horizontal = ['tags']


@admin.register(ChannelPlaylist)
class ChannelPlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    search_fields = ['name']
    date_hierarchy = 'created_on'


@admin.register(ChannelTag)
class ChannelTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
