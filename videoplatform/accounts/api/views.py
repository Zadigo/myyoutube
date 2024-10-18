from accounts.api import serializers
from accounts.models import CustomUser
from rest_framework.decorators import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response


class BaseAccountDetails(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = None
    permission_classes = []


class UpdateNotifications(APIView):
    http_method_names = ['get', 'post']
    serializer_class = serializers.UserSerializer
    validation_serializer_class = serializers.ValidateUpdateNotifications
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer(self, request):
        return self.serializer_class(instance=request.user)

    def get(self, request, **kwargs):
        user_serializer = self.get_serializer(request)
        return Response(user_serializer.data)

    def post(self, request, **kwargs):
        serializer = serializers.ValidateUpdateNotifications(
            instance=request.user,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user_serializer = self.get_serializer(request)
        return Response(user_serializer.data)
