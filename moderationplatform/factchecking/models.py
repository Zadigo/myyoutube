from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from moderationplatform.utils import create_id


class Vote(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='votes_cast',
        help_text="Votes cast by other fact checking members"
    )
    report = models.ForeignKey(
        'Report',
        on_delete=models.CASCADE,
        related_name='votes'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user_id + " - " + self.report.reference


class Source(models.Model):
    """Sources are urls or references that can be used
    to support fact checking reports. Sources have to follow
    a set of guidelines to be considered valid:

    - The source must be a valid URL
    - The source must be unique
    - The source must be credible, meaning it should come from a reputable organization or individual
    - The source must be relevant to the report it is being used for
    - The source must be accessible to the public
    - The source must not be a personal opinion or a blog post
    - The source must not be a social media post or a comment
    - The source must not be a video or audio file
    - The source must not be a screenshot or an image
    - The source must not be a link to a private or restricted content
    - The source must not be a link to a website that is not accessible
    """
    reference = models.CharField(
        max_length=255,
        unique=True
    )
    url = models.URLField(
        max_length=255,
        unique=True,
        validators=[]
    )
    source_credibility = models.PositiveIntegerField(
        default=0,
        help_text="Credibility score of the source, from 0 to 100"
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.reference


class Report(models.Model):
    """Reports are direct contributions from users
    that can be used to fact check content on videos 
    on the platform. They can be used to report
    misinformation, harmful content, or any other issues"""

    reference = models.CharField(
        max_length=255
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reports',
        help_text="User who created the report"
    )
    video_id = models.CharField(
        max_length=255
    )
    sources = models.ManyToManyField(
        Source,
        related_name='reports'
    )
    active = models.BooleanField(
        default=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.reference


@receiver(pre_save, sender=Vote)
def create_vote_reference(instance, **kwargs):
    instance.reference = create_id('vo')


@receiver(pre_save, sender=Report)
def create_report_reference(instance, **kwargs):
    instance.reference = create_id('re')


@receiver(pre_save, sender=Source)
def create_source_reference(instance, **kwargs):
    instance.reference = create_id('so')
