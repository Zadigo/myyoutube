from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from comments.models import Comment, Reply
from ratings.choices import RatingFor, RatingTypes
from ratings.managers import RatingManager
from videos.models import Video
from notifications.models import Notification


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


@receiver(post_save, sender=Rating)
def notify_user(instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
            user=instance.user,
            video=instance.video
        )

        if instance.video is not None:
            notification.notificiation_type = 'Like'
            notification.save()
