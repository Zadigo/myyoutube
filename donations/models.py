from django.contrib.auth import get_user_model
from django.db import models
from donations.validators import donation_validator
from mychannel.models import UserChannel

MYUSER = get_user_model()

class Donation(models.Model):
    user = models.ForeignKey(
        MYUSER, 
        on_delete=models.SET_NULL, 
        null=True
    )
    user_channel = models.ForeignKey(
        UserChannel,
        on_delete=models.SET_NULL,
        null=True
    )
    value = models.PositiveIntegerField(
        default=5,
        validators=[donation_validator]
    )
    notes = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    cancellation_asked = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
