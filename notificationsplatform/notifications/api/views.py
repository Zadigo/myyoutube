from rest_framework.generics import RetrieveUpdateAPIView
from notifications.models import PreferredNotification
from rest_framework.permissions import IsAuthenticated
from notifications.api.serializers import PreferredNotificationSerializer


class NotificationProfile(RetrieveUpdateAPIView):
    queryset = PreferredNotification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PreferredNotificationSerializer

    def get_object(self):
        qs = super().get_queryset()
        return qs.get(user=self.request.user)
