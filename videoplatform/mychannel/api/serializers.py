from rest_framework import fields
from rest_framework.serializers import Serializer

from accounts.api.serializers import UserSerializer


class ChannelTagSerializer(Serializer):
    name = fields.CharField()


class UserChannelSerializer(Serializer):
    reference = fields.CharField()
    user = UserSerializer()
    name = fields.CharField()
    description = fields.CharField()
    banner = fields.ImageField()
    resized_banner = fields.ImageField()
    channel_thumbnail = fields.ImageField()
    category = fields.CharField()
    email = fields.CharField()
    instagram = fields.CharField()
    tiktok = fields.CharField()
    facebook = fields.CharField()
    subscribers = UserSerializer(many=True)
    is_verified = fields.BooleanField()
    created_on = fields.DateTimeField()


class BlockedChannelSerializer(Serializer):
    channel = UserChannelSerializer()
    user = UserSerializer()


class SearchSerializer(Serializer):
    video_name = fields.CharField(required=False)
    tags = fields.ListField()
