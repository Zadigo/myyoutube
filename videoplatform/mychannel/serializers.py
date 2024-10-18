from django.shortcuts import get_object_or_404
from rest_framework import fields
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from mychannel import models


def get_channel(request, reference):
    return get_object_or_404(models.UserChannel, reference=reference)


class ChannelTagsSerializer(Serializer):
    id = fields.IntegerField()
    name = fields.CharField()


class ChannelPlaylistsSerializer(Serializer):
    id = fields.IntegerField()


class ChannelSerializer(Serializer):
    """Serializer for a specific user channel"""

    id = fields.IntegerField()
    reference = fields.CharField()
    name = fields.CharField()
    number_of_subscribers = fields.IntegerField()
    number_of_playlists = fields.IntegerField()
    channelplaylist_set = ChannelPlaylistsSerializer(many=True)
    tags = ChannelTagsSerializer(many=True)


class ChannelPlaylistSerializer(Serializer):
    id = fields.IntegerField()
    name = fields.CharField()


class SearchSerializer(Serializer):
    video_name = fields.CharField(required=False)
    tags = fields.ListField()

    def get_response(self, instance, data):
        return {
            'reference': instance.reference,
            'results': data
        }

    def search(self, request, reference):
        from videos import serializers as videos_serializers
        channel = get_channel(request, reference)
        queryset = channel.video_set.active_videos()

        # Filter by video names
        video_name = self.validated_data.get('video_name', None)
        if video_name is not None:
            queryset = queryset.filter(title__iexact=video_name)

        # Filter by tags
        tags = self.validated_data.get('tags', [])
        if tags:
            queryset = queryset.filter(tags__name__in=tags)

        serializer = videos_serializers.VideoSerializer(
            instance=queryset,
            many=True
        )
        return self.get_response(channel, serializer.data)
