from community_notes.models import CommunityNote, CommunityNoteSource
from django.contrib import admin


@admin.register(CommunityNoteSource)
class CommunityNoteSourceAdmin(admin.ModelAdmin):
    list_display = ['reference', 'url', 'source_credibility', 'created_on']
    search_fields = ['reference', 'url']
    list_filter = ['source_credibility', 'created_on', 'updated_on']
    ordering = ['-created_on']
    readonly_fields = ['created_on', 'updated_on', 'reference']


@admin.register(CommunityNote)
class CommunityNoteAdmin(admin.ModelAdmin):
    list_display = ['reference', 'author', 'subject_creator_id', 'created_on']
    search_fields = ['author__username', 'title', 'description']
    filter_horizontal = ['note_sources']
    list_filter = ['created_on']
    ordering = ['-created_on']
    readonly_fields = [
        'created_on', 'reference',
        'upvotes', 'downvotes', 'score'
    ]
