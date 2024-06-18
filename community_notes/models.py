from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from myyoutube.utils import create_id


class NoteSource(models.Model):
    url = models.URLField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'NoteSource: {self.pk}'


class Note(models.Model):
    reference = models.CharField(
        max_length=100
    )
    note_sources = models.ManyToManyField(
        NoteSource
    )
    video = models.ForeignKey(
        'videos.Video',
        models.CASCADE
    )
    user = models.ForeignKey(
        'accounts.MyUser',
        models.CASCADE
    )
    votes = models.PositiveIntegerField(
        default=0
    )
    # is_validated = models.BooleanField(
    #     default=False,
    #     help_text=_(
    #         "Indicates that the note has been peer "
    #         "reviewed and can be displayed"
    #     )
    # )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Note: {self.pk}'
    
    @property
    def is_validated(self):
        return self.votes > 0


@receiver(pre_save, sender=Note)
def create_note_reference(instance, **kwargs):
    instance.reference = create_id('no')
