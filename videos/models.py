import datetime
import os
import secrets

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
from videos.utils import stories_directory_path, video_directory_path
from mychannel.models import ChannelPlaylist, UserChannel


from videos.choices import (CategoryChoices, CommentingStrategy,
                            LanguageChoices, VisibilityChoices)
from videos.managers import PlaylistManager, VideoManager

MYUSER = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    videos = models.ManyToManyField('Video', blank=True)
    visibility = models.CharField(
        max_length=50, 
        choices=VisibilityChoices.choices, 
        default=VisibilityChoices.PUBLIC
    )
    created_on = models.DateTimeField(auto_now_add=True)

    objects = PlaylistManager.as_manager()
    
    class Meta:
        indexes = [
            models.Index(fields=['name', 'user', 'visibility'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Video(models.Model):
    user = models.ForeignKey(MYUSER, on_delete=models.CASCADE)
    user_channel = models.ForeignKey(UserChannel, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.CharField(max_length=15, blank=True, unique=True)

    title = models.CharField(max_length=70)
    description = models.TextField(max_length=300)
    video = models.FileField(upload_to=video_directory_path)

    age_restricted = models.BooleanField(default=False)
    category = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        default=CategoryChoices.ENTERTAINMENT
    )
    tags = models.ManyToManyField(Tag, blank=True)
    visibility = models.CharField(
        max_length=50, 
        choices=VisibilityChoices.choices, 
        default=VisibilityChoices.PUBLIC
    )
    recording_date = models.DateTimeField(default=timezone.now)
    recording_location = models.CharField(max_length=100, blank=True, null=True)
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
    ratings_are_visible = models.BooleanField(default=True)

    channel_playlist = models.ForeignKey(ChannelPlaylist, on_delete=models.SET_NULL, blank=True, null=True)

    views = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)
    # slug = models.SlugField()
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk', 'created_on']
        indexes = [
            models.Index(fields=['title', 'category'])
        ]

    objects = VideoManager.as_manager()

    def __str__(self):
        return self.title

    def clean(self):
        if not self.reference:
            self.reference = secrets.token_hex(nbytes=5)

    def get_absolute_url(self):
        return reverse('videos:detail', args=[self.reference])

    def get_edit_absolute_url(self):
        return reverse('mychannel:settings:video', args=[self.user_channel.reference, self.reference])


@receiver(post_delete, sender=Video)
def delete_video(sender, instance, **kwargs):
    is_s3_backend = False
    try:
        is_s3_backend = settings.USE_S3
    except:
        pass

    if not is_s3_backend:
        if instance.url:
            if os.path.isfile(instance.url.path):
                os.remove(instance.url.path)
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
