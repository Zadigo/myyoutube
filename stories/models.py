import datetime
import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from stories.utils import stories_directory_path

MYUSER = get_user_model()


class Story(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50, blank=True, unique=True)
    video = models.FileField(upload_to=stories_directory_path)
    expires = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('stories')
        indexes = [
            models.Index(
                fields=['video']
            )
        ]

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.created_on:
            expires_on = self.created_on + datetime.timedelta(hours=24)
            self.expires = expires_on

        if not self.reference:
            self.reference = secrets.token_hex(nbytes=10)

    def is_expired(self):
        return self.created_on > self.expires

    def remaining_time_left(self):
        return (self.created_on - self.expires).days
