from django.contrib import admin

from factchecking.models import Report, Source, Vote

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reference', 'user', 'video_id', 'creaeted_on', 'active']
    search_fields = ['reference', 'user__youtube_id', 'video_id']
    list_filter = ['active', 'created_on']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['reference', 'url', 'source_credibility', 'created_on']
    search_fields = ['url']
    list_filter = ['status', 'created_on']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    search_fields = ['report__reference', 'user__youtube_id', 'user__username']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']
