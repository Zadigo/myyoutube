import calendar

from django.db.models import Q
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear, ExtractWeek
from django.utils.timezone import now
from rest_framework import fields
from rest_framework.serializers import Serializer
from accounts.api.serializers import UserSerializer
from mychannel.serializers import ChannelPlaylistSerializer, ChannelSerializer
from videos import choices


class VideoSerializer(Serializer):
    id = fields.IntegerField()
    reference = fields.CharField()
    user_channel = ChannelSerializer()
    video = fields.FileField()
    channel_playlist = ChannelPlaylistSerializer()


class SearchSerializer(Serializer):
    name = fields.CharField(required=False)
    this_year = fields.BooleanField(default=False)
    last_week = fields.BooleanField(default=False)
    this_month = fields.BooleanField(default=False)
    today = fields.BooleanField(default=False)

    def search(self, request):
        queryset = self.instance
        # Filter by name
        name = self.validated_data.get('name', None)
        if name is not None:
            queryset = self.instance.filter(title__icontains=name)

        current_date = now()

        if self.validated_data['this_year']:
            queryset = queryset.annotate(year=ExtractYear('recording_date'))
            queryset = queryset.filter(year=current_date.year)

        if self.validated_data['this_month']:
            queryset = queryset.annotate(
                month=ExtractMonth('recording_date'),
                year=ExtractYear('recording_date')
            )
            queryset = queryset.filter(
                month=current_date.month,
                year=current_date.year
            )

        if self.validated_data['last_week']:
            queryset = queryset.annotate(week=ExtractWeek('recording_date'))
            current_week = current_date.isocalendar().week
            queryset = queryset.filter(
                week=current_week - 1,
                year=current_date.year
            )

        if self.validated_data['today']:
            queryset = queryset.annotate(
                day=ExtractDay('recording_date'),
                year=ExtractYear('recording_date')
            )
            queryset = queryset.filter(
                day=current_date.day,
                year=current_date.year
            )

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


class ValidateUpdateViewingProfile(Serializer):
    account_type = fields.ChoiceField(
        choices.AccountTypes.choices,
        default=choices.AccountTypes.BASIC
    )
    subscriptions = None
    night_mode = fields.BooleanField(default=False)
    algorithm_decides = None
    recommend_popular_videos = None
    preferred_categories = None
    preferred_ad = None
    performance = None
    playlists_private = None
    subscriptions_private = None
    personalize_ads = None

    def update(self, instance, validated_data):
        setattr(instance, 'account_type', validated_data['account_type'])
        setattr(instance, 'night_mode', validated_data['night_mode'])
        instance.save()
        return instance
