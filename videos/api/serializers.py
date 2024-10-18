
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractWeek,
                                        ExtractYear, Now)
from django.utils.timezone import now
from rest_framework import fields
from rest_framework.serializers import Serializer

from accounts.api.serializers import UserSerializer
from mychannel.models import UserChannel
from mychannel.serializers import ChannelPlaylistSerializer, ChannelSerializer
from videos import choices
from videos.api import validators
from videos.models import Video
from videos.processing import get_video_metadata


class VideoSerializer(Serializer):
    id = fields.IntegerField()
    title = fields.CharField()
    video_id = fields.CharField()
    user_channel = ChannelSerializer()
    video = fields.FileField()
    channel_playlist = ChannelPlaylistSerializer()
    user = UserSerializer()


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


class SubcategoriesSerializer(Serializer):
    title = fields.CharField()


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


class ValidateVideoUpload(Serializer):
    video = fields.FileField(
        validators=[validators.validate_file]
    )
    title = fields.CharField(
        validators=[validators.validate_video_title]
    )
    description = fields.CharField()
    age_restricted = fields.BooleanField(
        default=False
    )
    category = fields.ChoiceField(
        choices.CategoryChoices.choices,
        default=choices.CategoryChoices.ENTERTAINMENT
    )
    # tags = fields.JSONField()
    recording_date = fields.DateTimeField(
        allow_null=True
    )
    recording_location = fields.CharField(
        allow_null=True
    )
    recording_language = fields.ChoiceField(
        choices.LanguageChoices.choices,
        default=choices.LanguageChoices.FRENCH
    )
    comment_strategy = fields.ChoiceField(
        choices.CommentingStrategy.choices,
        default=choices.CommentingStrategy.ALLOW_ALL_COMMENTS
    )
    ratings_are_visible = fields.BooleanField(
        default=True
    )
    channel_playlist = fields.CharField(
        allow_null=True
    )
    visibility = fields.ChoiceField(
        choices.VisibilityChoices.choices,
        default=choices.VisibilityChoices.PUBLIC
    )

    def save(self, request, **kwargs):
        setattr(self, '_request', request)
        return super().save(**kwargs)

    def create(self, validated_data):
        request = getattr(self, '_request')

        channel = UserChannel.objects.get(user=request.user)
        queryset = channel.channelplaylist_set.filter(
            name=validated_data['channel_playlist']
        )
        if queryset.exists():
            validated_data['channel_playlist'] = queryset.get()

        if validated_data['recording_date'] is None:
            validated_data['recording_date'] = now().date()

        instance = Video.objects.create(
            user=request.user,
            **validated_data
        )

        details = get_video_metadata(instance.video.path)
        instance.duration = details.duration
        instance.width = details.size[0]
        instance.height = details.size[1]
        instance.framerate = details.framerate
        instance.save()

        return instance
