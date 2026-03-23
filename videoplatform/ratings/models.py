from django.contrib.auth import get_user_model
from django.db import models

from ratings.choices import RatingFor, RatingTypes
from ratings.managers import RatingManager
from videos.models import Video


class Rating(models.Model):
    """Represents a rating for a video,
    a comment or a reply"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    comment = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    reply = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    rating_for = models.CharField(
        max_length=50,
        choices=RatingFor.choices,
        default=RatingFor.VIDEO
    )
    rating_type = models.CharField(
        max_length=50,
        choices=RatingTypes.choices,
        default=RatingTypes.LIKE
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    objects = RatingManager.as_manager()

    def __str__(self):
        return f'{self.user.id} - {self.video}'
