from notifications.models import Notification, PreferredNotification
from rest_framework.serializers import ModelSerializer


class PreferredNotificationSerializer(ModelSerializer):
    class Meta:
        model = PreferredNotification
        fields = [
            'subscribed_channel_activity', 'video_recommendation',
            'channel_activity', 'replies_activity', 'mentions', 'repost'
        ]



class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
