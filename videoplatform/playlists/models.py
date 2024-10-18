from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from videoplatform.utils import create_id
from playlists.managers import PlaylistManager
from videos.choices import VisibilityChoices

USER_MODEL = get_user_model()


class Playlist(models.Model):
    """Represents a user's playlist containing
    a set of videos saved to the given playlist
    """

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        blank=True
    )
    playlist_id = models.CharField(
        max_length=100,
        blank=True,
        unique=True
    )
    name = models.CharField(
        max_length=50
    )
    videos = models.ManyToManyField(
        'videos.Video',
        blank=True
    )
    is_intelligent = models.BooleanField(
        default=False
    )
    visibility = models.CharField(
        max_length=50,
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.PUBLIC
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    objects = PlaylistManager.as_manager()

    class Meta:
        indexes = [
            models.Index(
                condition=models.Q(visibility='Public'),
                fields=['visibility'],
                name='visible_playlists'
            ),
            models.Index(
                condition=models.Q(is_intelligent=True),
                fields=['is_intelligent'],
                name='intelligent_playlists'
            )
        ]

    def __str__(self):
        return f'Playlist: {self.name}'


@receiver(pre_save, sender=Playlist)
def create_playlist_id(instance, **kwargs):
    if instance.playlist_id is None:
        instance.playlist_id = create_id('ply')
