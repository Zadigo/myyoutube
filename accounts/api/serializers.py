from django.contrib.auth import authenticate
from rest_framework import fields
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import Serializer


class UserSerializer(Serializer):
    id = fields.IntegerField()
    firstname = fields.CharField()
    lastname = fields.CharField()
    get_full_name = fields.CharField()


class TokenSerializer(Serializer):
    """Represents an authentication token"""
    key = fields.CharField()
    created = fields.DateTimeField()


class ValidateLoginSerializer(Serializer):
    email = fields.EmailField()
    password = fields.CharField()

    def save(self, request, **kwargs):
        setattr(self, 'request', request)
        return super().save(**kwargs)

    def create(self, validated_data):
        user = authenticate(
            getattr(self, 'request'),
            email=validated_data['email'],
            password=validated_data['password']
        )

        if user is None:
            raise AuthenticationFailed(detail='Could not authenticate user')

        if not user.is_active:
            raise AuthenticationFailed(detail='User is not active')

        auth_token, _ = Token.objects.get_or_create(user=user)
        return auth_token


class ValidateUpdateNotifications(Serializer):
    channel_activities = fields.BooleanField(default=False)
