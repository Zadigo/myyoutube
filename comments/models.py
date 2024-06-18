from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from videos.models import Video

USER_MODEL = get_user_model()


class AbstractComment(models.Model):
    video = models.ForeignKey(
        Video, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        USER_MODEL, 
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=500)
    from_creator = models.BooleanField(
        default=False,
        help_text=_('Comment written by the content creator')
    )
    pinned = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True


class Comment(AbstractComment):
    """Represents a base comment"""

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment: {self.user}'
    
    @property
    def number_of_replies(self):
        """Returns the number of replies
        for the given comment"""
        return self.reply_set.count()


class Reply(AbstractComment):
    """Represents a reply to a comment"""
    video = None
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('reply')
        verbose_name_plural = _('replies')
        ordering = ['-created_on']

    def __str__(self):
        return f'Reply: {self.user}'
