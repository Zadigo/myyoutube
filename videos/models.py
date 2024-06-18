import datetime
import os
import pathlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import (post_delete, post_save, pre_delete,
                                      pre_save)
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from mychannel.models import ChannelPlaylist, UserChannel
from myyoutube.utils import create_id
from videos import choices
from videos.choices import (CategoryChoices, CommentingStrategy,
                            LanguageChoices, VisibilityChoices)
from videos.managers import PlaylistManager, VideoManager
from videos.utils import stories_directory_path, video_directory_path

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
    """Represents a user's playlist"""

    user = models.ForeignKey(
        MYUSER, 
        on_delete=models.CASCADE, 
        blank=True
    )
    name = models.CharField(
        max_length=50
    )
    videos = models.ManyToManyField(
        'Video', 
        blank=True
    )
    visibility = models.CharField(
        max_length=50,
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.PUBLIC
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    objects = PlaylistManager.as_manager()

    class Meta:
        indexes = [
            # TODO: Remove
            models.Index(fields=['name', 'user', 'visibility'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Video(models.Model):
    """Represents the details for a given
    video uploaded on the plateform"""

    user = models.ForeignKey(
        MYUSER,
        on_delete=models.CASCADE
    )
    video_id = models.CharField(
        max_length=15,
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
            )
        ]

    def __str__(self):
        return f'Video: {self.title}'

    def clean(self):
        if not self.reference:
            self.reference = f'vid_{get_random_string(5)}'

    def get_absolute_url(self):
        return reverse('videos:detail', args=[self.reference])

    def get_edit_absolute_url(self):
        return reverse('mychannel:settings:video', args=[self.user_channel.reference, self.reference])


class Subscription(models.Model):
    pass


class PreferredAd(models.Model):
    alcohol = models.BooleanField(default=True)
    dating = models.BooleanField(default=True)
    gambling = models.BooleanField(default=True)
    pregnancy_parenting = models.BooleanField(default=True)
    weight_loss = models.BooleanField(default=True)

    def __str__(self):
        return f'Ad preference: {self.pk}'


class PreferredCategory(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    sub_category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class ViewingProfile(models.Model):
    """Encapsulates the different settings that adjusts
    the user viewing experience on the platform"""

    user = models.ForeignKey(
        MYUSER,
        models.CASCADE,
    )
    account_type = models.CharField(
        max_length=100,
        choices=choices.AccountTypes.choices,
        default=choices.AccountTypes.BASIC
    )
    subscriptions = models.ManyToManyField(
        Subscription,
        blank=True
    )
    night_mode = models.BooleanField(
        default=False
    )
    algorithm_decides = models.BooleanField(
        default=False,
        help_text=_("Let's the algorithm decide relevant videos")
    )
    recommend_popular_videos = models.BooleanField(
        default=False,
        help_text=_(
            "Recommend popular videos based on viewing "
            "history and currently viewed video"
        )
    )
    preferred_categories = models.ManyToManyField(
        PreferredCategory,
        help_text=_("Categories the user prefers to watch"),
        related_name='preferred_categories',
        blank=True
    )
    preferred_ad = models.ForeignKey(
        PreferredAd,
        models.CASCADE,
        related_name='preferred_ad',
        blank=True,
        null=True
    )
    performance = models.CharField(
        max_length=100,
        choices=choices.Performance.choices,
        default=choices.Performance.AUTO
    )
    playlists_private = models.BooleanField(
        default=False
    )
    subscriptions_private = models.BooleanField(
        default=False
    )
    personalize_ads = models.BooleanField(
        default=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'preferred_ad'],
                name='one_preferred_ad_by_user'
            )
        ]

    def __str__(self):
        return f'Viewing profile: {self.user}'


@receiver(pre_save, sender=Video)
def create_video_id(instance, **kwargs):
    if instance.video_id is None:
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


# @receiver(post_save, sender=MYUSER)
# def create_viewing_profile(instance, created, **kwargs):
#     if created:
#         profile = ViewingProfile.objects.create(user=instance)
#         profile.preferred_ad_set.create()
