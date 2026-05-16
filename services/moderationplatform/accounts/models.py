from django.contrib.auth.models import AbstractUser
from django.db import models


class ModerationUser(AbstractUser):
    """Custom user model for the moderation platform"""
    
    youtube_id = models.CharField(
        max_length=255,
        unique=True,
        help_text="Unique identifier for the user on YouTube"
    )
    
    def __str__(self):
        return self.username
