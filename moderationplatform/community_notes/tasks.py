from celery import shared_task
from celery.utils.log import get_task_logger
from community_notes.models import (CommunityNote, CommunityNoteSource,
                                    CommunityNoteVote)
from django.db import models
from django.core.cache import cache

logger = get_task_logger(__name__)


@shared_task
def verify_source_credibility(source_id: str, url: str):
    try:
        logic = (
            models.Q(source_id=source_id) |
            models.Q(id=source_id) |
            models.Q(url=url)
        )
        instance = CommunityNoteSource.objects.get(logic)
    except CommunityNoteSource.DoesNotExist:
        logger.error(f'Source with id {source_id} does not exist.')
        return

    list_of_trusted_domains = ['trustednews.com', 'reliableinfo.org']
    list_of_untrusted_domains = ['fakenews.net', 'unreliableinfo.biz']

    domain = instance.url.split('//')[-1].split('/')[0].replace('www.', '')

    if domain in list_of_trusted_domains:
        instance.source_credibility = 100
    elif domain in list_of_untrusted_domains:
        instance.source_credibility = 0
    else:
        instance.source_credibility = 50
    instance.save()

    logger.info(
        f'Updated source credibility for {instance.reference} to {instance.source_credibility}.')




@shared_task
def calculate_votes_for_note(note_id: str):
    """Task to calculate the total votes for a community note in order to
    cache the result for faster retrieval and display"""
    try:
        note = CommunityNote.objects.get(id=note_id)
    except CommunityNote.DoesNotExist:
        logger.error(f'CommunityNote with id {note_id} does not exist.')
        return

    votes = CommunityNoteVote.objects.filter(note=note)
    upvotes = votes.filter(value=1).count()
    downvotes = votes.filter(value=-1).count()
    total_score = upvotes - downvotes

    note.vote_score = total_score
    note.save()

    cache_key = f'note_vote_score_{note_id}'
    cache.set(cache_key, total_score, timeout=3600)  # Cache for 1 hour

    logger.info(
        f'Calculated votes for note {note.reference}: Upvotes={upvotes}, '
        f'Downvotes={downvotes}, Total Score={total_score}.'
    )
