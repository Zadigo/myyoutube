import os
import pathlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mychannel.models import ChannelPlaylist, UserChannel
from videos import choices
from videos.choices import (CategoryChoices, CommentingStrategy,
                            LanguageChoices, VisibilityChoices)
from videos.managers import VideoManager
from videos.utils import video_directory_path

from videoplatform.utils import create_id


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Video(models.Model):
    """Represents the details for a given
    video uploaded on the plateform"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    video_id = models.CharField(
        max_length=100,
        blank=True,
        unique=True
    )
    user_channel = models.ForeignKey(
        UserChannel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=70,
        validators=[]
    )
    description = models.TextField(
        max_length=300,
        validators=[]
    )
    video = models.FileField(
        upload_to=video_directory_path
    )
    age_restricted = models.BooleanField(
        default=False
    )
    category = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        default=CategoryChoices.ENTERTAINMENT
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    visibility = models.CharField(
        max_length=50,
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.PUBLIC
    )
    recording_date = models.DateTimeField(
        default=timezone.now
    )
    recording_location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    recording_language = models.CharField(
        max_length=50,
        choices=LanguageChoices.choices,
        default=LanguageChoices.ENGLISH
    )
    comment_strategy = models.CharField(
        max_length=150,
        choices=CommentingStrategy.choices,
        default=CommentingStrategy.ALLOW_ALL_COMMENTS
    )
    ratings_are_visible = models.BooleanField(
        default=True
    )
    channel_playlist = models.ForeignKey(
        ChannelPlaylist,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    framerate = models.FloatField(
        default=0
    )
    duration = models.FloatField(
        default=0
    )
    width = models.PositiveIntegerField(
        default=0
    )
    height = models.PositiveIntegerField(
        default=0
    )
    views = models.PositiveIntegerField(
        default=0
    )
    active = models.BooleanField(
        default=True
    )
    # slug = models.SlugField()
    modified_on = models.DateTimeField(
        auto_now=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    objects = VideoManager.as_manager()

    class Meta:
        ordering = ['-pk', 'created_on']
        indexes = [
            models.Index(
                fields=['active'],
                name='active_videos',
                condition=models.Q(active=True)
            ),
            models.Index(
                fields=['visibility'],
                name='visible_videos',
                condition=models.Q(visibility=True)
            ),
            models.Index(
                fields=['active', 'visibility'],
                name='active_and_visible_videos',
                condition=(
                    models.Q(visibility=True) &
                    models.Q(active=True)
                )
            ),
            models.Index(
                fields=['duration'],
                name='less_than_ten_minutes',
                condition=(
                    models.Q(duration__lte=10) &
                    models.Q(active=True)
                )
            )
        ]

    def __str__(self):
        return f'Video: {self.title}'

    def get_absolute_url(self):
        return reverse('videos:detail', args=[self.reference])

    def get_edit_absolute_url(self):
        return reverse('mychannel:settings:video', args=[self.user_channel.reference, self.reference])


@receiver(pre_save, sender=Video)
def create_video_id(instance, **kwargs):
    if not instance.video_id:
        instance.video_id = create_id('vid')


@receiver(post_delete, sender=Video)
def delete_video(sender, instance, **kwargs):
    is_s3_backend = getattr(settings, 'USE_S3', False)

    if not is_s3_backend:
        if instance.url:
            path = pathlib.Path(instance.url.path)
            if path.exists() and path.is_file():
                path.unlink()
            # if os.path.isfile(instance.url.path):
            #     os.remove(instance.url.path)
    else:
        instance.url.delete(save=False)


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
                old_video = Video.objects.get(pk=instance.pk)
            except:
                return False
            else:
                new_video = instance.url
                if old_video and old_video != new_video:
                    if os.path.isfile(old_video.url.path):
                        os.remove(old_video.url.path)
    else:
        instance.url.delete(save=False)
