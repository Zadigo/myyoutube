import calendar

from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractWeek,
                                        ExtractYear, Now)
from django.utils.timezone import now
from rest_framework import fields
from rest_framework.serializers import Serializer

from accounts.api.serializers import UserSerializer
from mychannel.serializers import ChannelPlaylistSerializer, ChannelSerializer
from videos import choices
from videos.api import validators


class VideoSerializer(Serializer):
    id = fields.IntegerField()
    video_id = fields.CharField()
    user_channel = ChannelSerializer()
    video = fields.FileField()
    channel_playlist = ChannelPlaylistSerializer()


class SearchSerializer(Serializer):
    name = fields.CharField(required=False)
    tags = None
    username = None
    channel = None
    age_restricted = None
    category = None
    recorded_on = None
    recorded_after = None
    recorded_before = None
    created_on = None
    this_year = fields.BooleanField(default=False)
    last_week = fields.BooleanField(default=False)
    this_month = fields.BooleanField(default=False)
    today = fields.BooleanField(default=False)

    def search(self, request):
        queryset = self.instance

        name = self.validated_data.get('name')
        if name is not None:
            queryset = self.instance.filter(title__icontains=name)

        current_date = now()
        queryset = queryset.annotate(
            day=ExtractDay('recording_date'),
            week=ExtractWeek('recording_date'),
            month=ExtractMonth('recording_date'),
            year=ExtractYear('recording_date')
        )

        if self.validated_data.get('this_year'):
            queryset = queryset.filter(year=current_date.year)

        if self.validated_data.get('this_month'):
            queryset = queryset.filter(
                month=current_date.month,
                year=current_date.year
            )

        if self.validated_data.get('last_week'):
            current_week = current_date.isocalendar().week
            queryset = queryset.filter(
                week=current_week - 1,
                year=current_date.year
            )

        if self.validated_data.get('today'):
            queryset = queryset.filter(create_on=Now())

        instance = VideoSerializer(instance=queryset, many=True)
        return instance.data


class ViewingProfileSerializer(Serializer):
    id = fields.IntegerField()
    user = UserSerializer()
    account_type = fields.CharField()
    subscriptions = None
    night_mode = fields.BooleanField()
    algorithm_decides = None
    recommend_popular_videos = None
    preferred_categories = None
    preferred_ad = None
    performance = None
    playlists_private = None
    subscriptions_private = None
    personalize_ads = None


class ValidateViewingProfile(Serializer):
    account_type = fields.ChoiceField(
        choices.AccountTypes.choices,
        default=choices.AccountTypes.BASIC
    )
    subscriptions = None
    night_mode = fields.BooleanField(default=False)
    algorithm_decides = None
    recommend_popular_videos = fields.BooleanField(
        default=True
    )
    preferred_categories = None
    preferred_ad = None
    performance = None
    playlists_private = None
    subscriptions_private = None
    personalize_ads = None
    blocked_channels = fields.JSONField()
    blocked_keywords = fields.JSONField(
        validators=[validators.validate_keywords]
    )

    def update(self, instance, validated_data):
        setattr(instance, 'account_type', validated_data['account_type'])
        setattr(instance, 'night_mode', validated_data['night_mode'])
        instance.save()
        return instance
