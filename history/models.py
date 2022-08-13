from django.contrib.auth import get_user_model
from django.db import models
from videos.models import Video

MYUSER = get_user_model()

class History(models.Model):
    user  = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Histories'
        ordering = ['created_on', '-pk']
        indexes = [
            models.Index(fields=['video'])
        ]

    def __str__(self):
        return self.video.title
