from django.contrib import admin

from videos.models import Video, Tag, Playlist


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'visibility', 'created_on']
    search_fields = ['title', 'category', 'visibility']
    date_hierarchy = 'created_on'
    actions = ['activate', 'deactivate']

    def activate(self, queryset):
        return queryset.update(active=True)

    def deactivate(self, queryset):
        return queryset.update(active=False)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'visibility', 'created_on']
    search_fields = ['name', 'user__username', 'visibility']
    sortable_by = ['name', 'visibility']
    filter_horizontal = ['videos']
    date_hierarchy = 'created_on'
        