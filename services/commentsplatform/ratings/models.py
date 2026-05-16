from comments.models import Comment, Reply
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ratings.choices import RatingFor, RatingTypes
from ratings.managers import RatingManager


class Rating(models.Model):
    """Represents a rating for a video,
    a comment or a reply"""

    user = models.ForeignKey(
        get_user_model(),
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
    rating_for = models.CharField(
        max_length=50,
        choices=RatingFor.choices,
        default=RatingFor.COMMENT
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
        return f'{self.user.id} - {self.comment}'
