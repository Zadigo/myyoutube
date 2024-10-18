from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mychannel import models, serializers
from videos.api import serializers as videos_serializers


def get_channel(request, reference):
    return get_object_or_404(models.UserChannel, reference=reference)


@api_view(['post'])
def channels_view(request, **kwargs):
    channels = models.UserChannel.objects.filter().order_by('created_on')
    serializer = serializers.ChannelSerializer(instance=channels, many=True)
    return Response(serializer.data)


@api_view(['post'])
def channel_view(request, reference, **kwargs):
    """Returns the details for a given channel"""
    channel = get_object_or_404(models.UserChannel, reference=reference)
    serializer = serializers.ChannelSerializer(instance=channel)
    return Response(serializer.data)


@api_view(['post'])
def search_videos_view(request, reference, **kwargs):
    search_serializer = serializers.SearchSerializer(data=request.data)
    search_serializer.is_valid(raise_exception=True)

    # channel = get_channel(request, reference)
    # videos = channel.video_set.all()
    # serializer = videos_serializers.VideoSerializer(
    #     instance=videos,
    #     many=True
    # )
    data = search_serializer.search(request, reference)
    return Response(data)
