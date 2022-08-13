from django.contrib.auth import get_user_model
from django.db import models

from videos.models import Video
from notifications.choices import NotificationTypes

MYUSER = get_user_model()

class Notification(models.Model):
    user    = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    video  = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    notification_type = models.CharField(
        max_length=50,
        choices=NotificationTypes.choices,
        default=NotificationTypes.FOLLOW
    )
    read        = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created_on', '-pk']

    def __str__(self):
        return self.user.username
