from django.contrib import admin

from moderationplatform.community_notes.models import Note, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['reference', 'url', 'source_credibility', 'created_on']
    search_fields = ['reference', 'url']
    list_filter = ['source_credibility', 'created_on', 'updated_on']
    ordering = ['-created_on']
    readonly_fields = ['created_on', 'updated_on', 'reference']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'created_on']
    search_fields = ['user__username', 'content']
    list_filter = ['created_on']
    ordering = ['-created_on']
    readonly_fields = ['created_on', 'updated_on', 'reference']
