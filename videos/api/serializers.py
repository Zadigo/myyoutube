import calendar

from django.db.models import Q
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractWeek,
                                        ExtractYear)
from django.utils.timezone import now
from rest_framework import fields
from rest_framework.serializers import Serializer

from mychannel.serializers import ChannelPlaylistSerializer, ChannelSerializer


class VideoSerializer(Serializer):
    id = fields.IntegerField()
    video_id = fields.CharField()
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
