from rest_framework.serializers import Serializer
from rest_framework import fields


class UserSerializer(Serializer):
    id = fields.IntegerField()
    firstname = fields.CharField()
    lastname = fields.CharField()


class ValidateUpdateNotifications(Serializer):
    channel_activities = fields.BooleanField(default=False)
