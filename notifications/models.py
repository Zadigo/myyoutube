from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models

from videos.models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications.choices import NotificationTypes

MYUSER = get_user_model()


class Notification(models.Model):
    """Represents a user notification"""
    user = models.ForeignKey(
        MYUSER,
        on_delete=models.CASCADE,
        help_text=_('User to notify')
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    notification_type = models.CharField(
        max_length=50,
        choices=NotificationTypes.choices,
        default=NotificationTypes.FOLLOW
    )
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on', '-pk']

    def __str__(self):
        return self.user.username


class PreferredNotification(models.Model):
    """Reprsents notification choices for
    a given user"""
    user = models.ForeignKey(
        MYUSER,
        models.CASCADE
    )
    subscribed_channel_activity = models.BooleanField(default=True)
    video_recommendation = models.BooleanField(default=True)
    channel_activity = models.BooleanField(default=True)
    replies_activity = models.BooleanField(default=True)
    mentions = models.BooleanField(default=True)
    repost = models.BooleanField(
        default=True,
        help_text=_("When other users repost the user's content")
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                name='one_notification_choice_per_user'
            )
        ]

    def __str__(self):
        return f'Notification choices: {self.user}'


@receiver(post_save, sender=MYUSER)
def create_notification_choices(instance, created, **kwargs):
    if created:
        PreferredNotification.objects.create(user=instance)
