import secrets

from django.contrib.auth import get_user_model
from django.db import models
from stories.models import Story

from videos.models import Video

from mediastats.managers import StatisticsManager

MYUSER = get_user_model()

class MediaView(models.Model):
    reference = models.CharField(max_length=100, blank=True, unique=True)
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE, blank=True, null=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.FloatField(default=0.0)
    ended_at = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = StatisticsManager().as_manager()

    def __str__(self):
        return self.reference

    def clean(self):
        if not self.reference:
            self.reference = secrets.token_hex(nbytes=5)

    def get_media_type(self):
        if self.story:
            return 'Story'
        return 'Video'
