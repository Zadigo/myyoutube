import secrets

from comments.models import Comment, Reply
from django.contrib.auth import get_user_model
from django.db import models
from reports.choices import ReportTypes
from videos.models import Video


class Report(models.Model):
    """Represents a report on a video, comment, or reply
    with a reference ID, user who reported it,
    and the category of the report"""

    reference = models.CharField(
        max_length=100,
        default=secrets.token_hex(10),
        unique=True
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='reported_by'
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    reply = models.ForeignKey(
        Reply,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    category = models.CharField(
        max_length=50,
        choices=ReportTypes.choices,
        default=ReportTypes.SEXISM
    )
    notes = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    is_correct = models.BooleanField(
        default=False
    )
    reviewed = models.BooleanField(
        default=False
    )
    reviewed_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    reviewed_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.video.title
