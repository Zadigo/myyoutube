from django.db import models


class Source(models.Model):
    reference = models.CharField(
        max_length=255,
        unique=True
    )
    url = models.URLField(
        max_length=255, 
        unique=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )


class Report(models.Model):
    reference = models.CharField(
        max_length=255
    )
    user_id = models.CharField(
        max_length=255
    )
    video_id = models.CharField(
        max_length=255
    )
    sources = models.ManyToManyField(
        Source, 
        related_name='reports'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
