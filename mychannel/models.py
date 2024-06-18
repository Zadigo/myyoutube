import os
import pathlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from mychannel.choices import ChannelCategories
from mychannel.utils import banners_directory_path
from myyoutube.utils import create_id

MYUSER = get_user_model()


class ChannelTag(models.Model):
    """Represents a classification 
    tag for the channel"""
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class ChannelPlaylist(models.Model):
    """Represents a playlist for a channel"""

    user_channel = models.ForeignKey('UserChannel', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = None
    addition_type = None
    active = None
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class UserChannel(models.Model):
    """Represents a user's channel. A channel can
    be defined a space in which the user can reunite
    all the videos that has uploaded on the plateform"""

    reference = models.CharField(
        max_length=50,
        unique=True
    )
    user = models.ForeignKey(
        MYUSER,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=2000
    )
    banner = models.ImageField(
        upload_to=banners_directory_path,
        blank=True,
        null=True
    )
    resized_banner = ImageSpecField(
        source='banner',
        processors=[ResizeToFill(width=1200, height=500)],
        format='JPEG',
        options={'quality': 80}
    )
    channel_thumbnail = ImageSpecField(
        source='banner',
        processors=[ResizeToFill(width=400, height=400)],
        format='JPEG',
        options={'quality': 60}
    )
    category = models.CharField(
        max_length=100,
        choices=ChannelCategories.choices,
        default=ChannelCategories.BEAUTY
    )

    email = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    instagram = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    tiktok = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    facebook = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    subscribers = models.ManyToManyField(
        MYUSER,
        related_name='channel_subscribers',
        blank=True
    )
    is_verified = models.BooleanField(
        default=False
    )
    tags = models.ManyToManyField(
        ChannelTag,
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']
        indexes = [
            models.Index(
                fields=['is_verified'],
                name='verified_channel',
                condition=models.Q(is_verified=True)
            )
        ]

    def __str__(self):
        return f'UserChannel: {self.name}'

    def get_absolute_url(self):
        return reverse('mychannel:detail', args=[self.reference])

    @cached_property
    def number_of_subscribers(self):
        """Returns the number of subscribers
        for the current given channel"""
        return self.subscribers.count()

    @cached_property
    def number_of_playlists(self):
        """Returns the number of playlists for the
        current given channel"""
        return self.channelplaylist_set.count()


class BlockedChannel(models.Model):
    """Represents channels blocked by the viewer"""
    channel = models.ForeignKey(
        UserChannel,
        models.CASCADE,
        blank=True
    )
    user = models.ForeignKey(
        MYUSER,
        models.CASCADE,
        blank=True
    )

    def __str__(self):
        return f'{self.channel} blocked by: {self.user}'


@receiver(pre_save, sender=UserChannel)
def create_channel_id(instance, **kwargs):
    if not instance.reference:
        instance.reference = create_id('ch')


# @receiver(post_delete, sender=UserChannel)
# def delete_channel_videos(sender, instance, **kwargs):
#     s3_backend = getattr(settings, 'USE_S3', False)

#     if not s3_backend:
#         if instance.url is not None:
#             path = pathlib.Path(instance.url.path)
#             if path.exists() and path.is_file():
#                 path.unlink()
#     else:
#         instance.url.delete(save=False)

    # is_s3_backend = False
    # try:
    #     is_s3_backend = settings.USE_S3
    # except:
    #     pass

    # if not is_s3_backend:
    #     if instance.url:
    #         if os.path.isfile(instance.url.path):
    #             os.remove(instance.url.path)
    # else:
    #     instance.url.delete(save=False)


# @receiver(pre_delete, sender=Video)
def delete_videos(sender, instance, **kwargs):
    videos = instance.images.all()
    for video in videos:
        if video.url:
            if os.path.isfile(video.url.path):
                os.remove(video.url.path)


# @receiver(pre_save, sender=Video)
def delete_video_on_update(sender, instance, **kwargs):
    is_s3_backend = False
    try:
        is_s3_backend = settings.USE_S3
    except:
        pass

    if not is_s3_backend:
        if instance.pk:
            try:
                old_video = UserChannel.objects.get(pk=instance.pk)
            except:
                return False
            else:
                new_video = instance.url
                if old_video and old_video != new_video:
                    if os.path.isfile(old_video.url.path):
                        os.remove(old_video.url.path)
    else:
        instance.url.delete(save=False)
