from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from videos.choices import VisibilityChoices
from videos import models, serializers


@api_view(['post'])
def get_videos(request, **kwargs):
    queryset = models.Video.objects.all()
    serializer = serializers.VideoSerializer(instance=queryset, many=True)
    # serializer.is_valid(raise_exception=True)
    return Response(serializer.data)


@api_view(['post'])
def get_video(request, reference, **kwargs):
    video = get_object_or_404(models.Video, reference=reference)
    serializer = serializers.VideoSerializer(instance=video)
    return Response(serializer.data)



@api_view(['post'])
def search_videos(request, **kwargs):
    queryset = models.Video.objects.active_videos()
    serializer = serializers.SearchSerializer(instance=queryset, data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.search(request)
    return Response(data)
