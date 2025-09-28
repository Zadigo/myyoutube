from notifications import tasks
from notifications.api import serializers
from notifications.api.serializers import PreferredNotificationSerializer
from notifications.models import Notification, PreferredNotification
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListNotifications(ListAPIView):
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NotificationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).order_by('-created_on')


class NotificationProfile(RetrieveUpdateAPIView):
    queryset = PreferredNotification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PreferredNotificationSerializer

    def get_object(self):
        qs = super().get_queryset()
        return qs.get(user=self.request.user)


class CreateNotification(GenericAPIView):
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NotificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tasks.add_notification.apply_async(
            kwargs={
                'user_id': request.user.id,
                'validated_data': serializer.validated_data
            }
        )

        return Response({}, status=201)
