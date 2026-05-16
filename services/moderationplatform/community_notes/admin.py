from community_notes.models import CommunityNote, CommunityNoteVote
from django.contrib import admin


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


@admin.register(CommunityNoteVote)
class CommunityNoteVoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'value']
    search_fields = [
        'note__reference', 'note__title', 'note__description',
        'note__subject_creator_id', 'user__username', 'user__email'
    ]
    readonly_fields = ['created_on', 'value', 'note', 'user']
    list_filter = ['created_on']
    ordering = ['-created_on']
