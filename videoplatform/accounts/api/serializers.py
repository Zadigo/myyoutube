from accounts.models import (PreferredAd, PreferredCategory, UserProfile,
                             ViewingProfile)
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer


class UserSerializer(Serializer):
    id = fields.IntegerField()
    firstname = fields.CharField()
    lastname = fields.CharField()
    username = fields.CharField()
    get_full_name = fields.CharField()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id', 'avatar', 'avatar_thumbnail',
            'birthdate', 'telephone', 'address',
            'city', 'zip_code', 'is_professional'
        ]


class PreferredAdSerializer(ModelSerializer):
    class Meta:
        model = PreferredAd
        fields = [
            'alcohol', 'dating',
            'gambling', 'pregnancy_parenting',
            'weight_loss'
        ]


class PreferredCategory(ModelSerializer):
    class Meta:
        model = PreferredCategory
        fields = ['name', 'sub_category']


class ViewingProfileCategory(ModelSerializer):
    class Meta:
        model = ViewingProfile
        fields = [
            'account_type', 'subscriptions',
            'night_mode', 'algorithm_decides',
            'recommend_popular_videos', 'preferred_categories',
            'performance', 'playlists_private', 'subscriptions_private',
            'personalize_ads'
        ]


class TokenSerializer(Serializer):
    """Represents an authentication token"""
    key = fields.CharField()
    created = fields.DateTimeField()


class ValidateUpdateNotifications(Serializer):
    channel_activities = fields.BooleanField(default=False)
