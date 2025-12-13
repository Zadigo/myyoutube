from community_notes.choices import NoteStatus
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from moderationplatform.utils import create_id


class CommunityNoteVote(models.Model):
    note = models.ForeignKey(
        'community_notes.CommunityNote',
        on_delete=models.CASCADE,
        related_name="votes"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    reason = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional reason applied only for downvotes"
    )
    value = models.SmallIntegerField(
        choices=(
            (1, "Upvote"),
            (-1, "Downvote")
        )
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('note', 'user')
        indexes = [
            models.Index(
                fields=['note', 'value']
            )
        ]

    def __str__(self):
        return f'NoteVote: Note {self.note.reference} by User {self.user.username}'


class CommunityNoteSource(models.Model):
    """Source model represents a source of information
    that can be used to support community notes"""

    reference = models.CharField(
        max_length=255,
        unique=True
    )
    url = models.URLField(
        max_length=255,
        unique=True,
        validators=[]
    )
    source_credibility = models.PositiveIntegerField(
        default=0,
        help_text="Credibility score of the source, from 0 to 100"
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'Source: {self.reference}'


class CommunityNote(models.Model):
    """Community notes are general contributions from users
    that can be used to provide additional context or information
    about a content creator and the overall direction of the content
    that is being created"""

    reference = models.CharField(
        max_length=100
    )
    title = models.CharField(
        max_length=255,
        help_text=_("Title of the community note")
    )
    description = models.TextField(
        max_length=2000,
        help_text=_("Content of the community note")
    )
    note_sources = models.ManyToManyField(
        CommunityNoteSource,
        related_name='notes',
        help_text=_("Sources that support the note")
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='notes_authored',
        help_text=_("User who authored the note")
    )
    subject_creator_id = models.CharField(
        max_length=100,
        help_text=_(
            "Unique identifier of the content "
            "creator this note is about"
        )
    )
    status = models.CharField(
        max_length=20,
        choices=NoteStatus.choices,
        default=NoteStatus.DRAFT,
        help_text=_("Current status of the community note")
    )
    upvotes = models.PositiveIntegerField(
        default=0
    )
    downvotes = models.PositiveIntegerField(
        default=0
    )
    score = models.IntegerField(
        default=0, 
        db_index=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['status', 'score']),
            models.Index(fields=['subject_creator_id', 'status']),
            models.Index(fields=['created_on'])
        ]

    def __str__(self):
        return f'Note: {self.reference}'

    # @property
    # def is_appproved(self):
    #     return self.votes > 100

    # @property
    # def vote_score(self):
    #     result = self.votenote_set.aggregate(score=models.Sum('value'))
    #     return result['score'] or 0


@receiver(post_save, sender=CommunityNote)
def create_note_reference(instance, created, **kwargs):
    if created and not instance.reference:
        instance.reference = create_id('no')
        instance.save()


@receiver(post_save, sender=CommunityNoteSource)
def create_source_reference(instance, created, **kwargs):
    if created and not instance.reference:
        instance.reference = create_id('so')
        instance.save()
