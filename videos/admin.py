from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _

from accounts.admin import custom_admin
from myyoutube.utils import create_id
from videos.models import (Playlist, PreferredAd, PreferredCategory,
                           Subscription, Tag, Video, ViewingProfile)
from videos.processing import get_video_metadata


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'visibility', 'created_on']
    search_fields = ['title', 'category', 'visibility']
    date_hierarchy = 'created_on'
    readonly_fields = ['video_id']
    actions = ['activate', 'deactivate',
               'generate_video_ids', 'get_metadata']

    def get_metadata(self, request, queryset):
        for item in queryset:
            details = get_video_metadata(item.video.path)
            item.width = details.size[0]
            item.height = details.size[1]
            item.framerate = details.framerate
            item.duration = details.duration
            item.save()

    def activate(self, queryset):
        return queryset.update(active=True)

    def deactivate(self, queryset):
        return queryset.update(active=False)

    def generate_video_ids(self, request, queryset):
        # if queryset.count() > 1:
        #     messages.error(request, 'Only select one video', fail_silently=True)
        #     return False

        for video in queryset:
            video.video_id = create_id('vid')
            video.save()

        message = _(f"Changed the id for {queryset.count()} videos")
        messages.success(request, message)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'visibility', 'created_on']
    search_fields = ['name', 'user__username', 'visibility']
    sortable_by = ['name', 'visibility']
    filter_horizontal = ['videos']
    date_hierarchy = 'created_on'


class ViewingProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_type']


class PreferredAdAdmin(admin.ModelAdmin):
    pass


class PreferredCategoryAdmin(admin.ModelAdmin):
    pass


custom_admin.register(Video, VideoAdmin)
custom_admin.register(Tag, TagAdmin)
custom_admin.register(Playlist, PlaylistAdmin)
custom_admin.register(ViewingProfile, ViewingProfileAdmin)
custom_admin.register(PreferredAd, PreferredAdAdmin)
custom_admin.register(PreferredCategory, PreferredCategoryAdmin)
