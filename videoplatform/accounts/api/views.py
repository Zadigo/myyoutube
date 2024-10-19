from accounts.api import serializers
from accounts.models import CustomUser, UserProfile, ViewingProfile
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response


class RetrieveMixin:
    permission_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__is_active=True)


class BaseAccountDetails(RetrieveMixin, RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=1)
        self.check_object_permissions(self.request, obj)
        return obj


class ViewingProfileDetails(RetrieveMixin, RetrieveUpdateAPIView):
    queryset = ViewingProfile.objects.all()
    serializer_class = serializers.ViewingProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=1)
        self.check_object_permissions(self.request, obj)
        return obj


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
