from django.contrib.auth import get_user_model
from django.db import models
from videos.models import Video

MYUSER = get_user_model()


class AbstractComment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    from_creator = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comment(AbstractComment):
    created_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.user.username


class Reply(AbstractComment):
    video = None
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Replies'

    def __str__(self):
        return self.user.username
