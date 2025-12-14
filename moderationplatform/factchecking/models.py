from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from reportsources.models import ReportSource

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
        ReportSource,
        related_name='reports'
    )
    # explanation = models.TextField(
    #     help_text="Explanation of the report"
    # )
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
