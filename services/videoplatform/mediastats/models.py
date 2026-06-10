from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from mediastats.managers import StatisticsManager
from stories.models import Story
from videos.models import Video


class MediaView(models.Model):
    """Collects the views for a given video"""

    reference = models.CharField(
        max_length=100,
        help_text=_('Unique reference for the view'),
        blank=True,
        unique=True
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        help_text=_('View for a story'),
        blank=True,
        null=True
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        help_text=_('View for a normal video'),
        blank=True,
        null=True
    )
    duration = models.FloatField(
        default=0.0,
        help_text=_('The actual video duration')
    )
    ended_at = models.FloatField(
        default=0.0,
        help_text=_('The total duration viewed by the user')
    )
    # skipped = models.BooleanField(
    #     default=False,
    #     help_text=_('Indicates whether a section of the video was skipped')
    # )
    created_on = models.DateTimeField(auto_now_add=True)

    objects = StatisticsManager.as_manager()

    def __str__(self):
        return f'View for {self.reference}'

    @property
    def is_story(self):
        return self.story is not None

    @cached_property
    def time_difference(self):
        """Returns the time difference between the
        total length of the video and the actual
        final timeframe where the video was stopped"""
        pass

    @cached_property
    def percentage_viewed(self):
        """Returns the percentage the of the
        video that was viewed"""
        pass

    @cached_property
    def decode_reference(self):
        _, reference, user, _ = self.reference.split('_')
        return reference, user

    def get_media_type(self):
        return 'Story' if self.is_story else 'Video'


@receiver(pre_save, sender=MediaView)
def create_reference(instance, **kwargs):
    # Create a unique reference for the view
    # using the base64 video ID and a random
    # string
    if instance.is_story:
        video_id = str(instance.story.id)
    else:
        video_id = str(instance.video.id)

    try:
        # TODO: Raises a bytes like error because
        # the ID is probably not set pre_save
        reference = urlsafe_base64_encode(video_id)
        user = urlsafe_base64_encode(str(instance.user.id))
    except:
        reference = f'vw_{get_random_string(length=12)}'
    else:
        salt = get_random_string(length=5)
        reference = f'vw_{reference}_{user}_{salt}'

    instance.reference = reference
