from notifications.api import serializers
from notifications.api.serializers import PreferredNotificationSerializer
from notifications.models import Notification, PreferredNotification
from rest_framework.generics import (RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated


class NotificationProfile(RetrieveUpdateAPIView):
    queryset = PreferredNotification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PreferredNotificationSerializer

    def get_object(self):
        qs = super().get_queryset()
        return qs.get(user=self.request.user)


class CreateNotificaton(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NotificationSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
