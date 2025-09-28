from rest_framework import fields
from notifications import choices
from notifications.models import Notification, PreferredNotification
from rest_framework.serializers import ModelSerializer, Serializer


class PreferredNotificationSerializer(ModelSerializer):
    class Meta:
        model = PreferredNotification
        fields = [
            'subscribed_channel_activity', 'video_recommendation',
            'channel_activity', 'replies_activity', 'mentions', 'repost'
        ]


class NotificationSerializer(Serializer):
    video = fields.CharField()
    notification_type = fields.ChoiceField(
        choices=choices.NotificationTypes.choices,
        default='Follow'
    )
