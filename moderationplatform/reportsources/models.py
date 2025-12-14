from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from moderationplatform.utils import create_id


class AbstractReportSource(models.Model):
    """Abstract base model for report sources"""

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
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class ReportSource(AbstractReportSource):
    """ReportSource model represents a source of information
    that can be used to support community notes"""

    def __str__(self):
        return f'Source: {self.reference}'


@receiver(post_save, sender=ReportSource)
def create_source_reference(instance, created, **kwargs):
    if created and not instance.reference:
        instance.reference = create_id('so')
        instance.save()
