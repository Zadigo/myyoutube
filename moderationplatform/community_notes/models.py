from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from moderationplatform.utils import create_id


class Source(models.Model):
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
        return self.reference


class Note(models.Model):
    """Community notes are general contributions from users
    that can be used to provide additional context or information
    about a content creator and the overall direction of the content
    that is being created"""

    reference = models.CharField(
        max_length=100
    )
    note_sources = models.ManyToManyField(
        Source,
        related_name='notes',
        help_text=_("Sources that support the note")
    )
    writer_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='notes_written',
        help_text=_("User who wrote the note")
    )
    creator_id = models.CharField(
        max_length=100,
        help_text=_("Unique identifier for the content creator on whom the note is written")
    )
    votes = models.PositiveIntegerField(
        default=0
    )
    is_validated = models.BooleanField(
        default=False,
        help_text=_(
            "Indicates that the note has been peer "
            "reviewed and can be displayed"
        )
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Note: {self.reference}'

    @property
    def is_validated(self):
        return self.votes > 0


@receiver(pre_save, sender=Note)
def create_note_reference(instance, **kwargs):
    instance.reference = create_id('no')
