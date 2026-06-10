from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from videos.models import Video


class History(models.Model):
    """Model that stores all the data for
    the current given user"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = _('histories')
        ordering = ['created_on', '-pk']
        indexes = [
            models.Index(
                fields=['video']
            )
        ]

    def __str__(self):
        return self.video.title
