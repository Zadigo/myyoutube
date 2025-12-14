from django.contrib import admin

from factchecking.models import FactCheck, Vote


@admin.register(FactCheck)
class FactCheckAdmin(admin.ModelAdmin):
    list_display = ['reference', 'video_id', 'created_on', 'active']
    search_fields = ['reference', 'author__youtube_id', 'video_id']
    filter_horizontal = ['factcheck_sources']
    list_filter = ['active', 'created_on']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    search_fields = ['report__reference', 'user__youtube_id', 'user__username']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']
