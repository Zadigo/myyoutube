from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from videos import models
from videos.api import serializers


@api_view(['post'])
def get_videos(request, **kwargs):
    """Returns all the videos from the plateform that
    are active and with visibility set to Public"""
    queryset = models.Video.objects.filter(
        active=True,
        visibility='Public'
    )
    serializer = serializers.VideoSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer.data)


@api_view(['post'])
def get_video(request, video_id, **kwargs):
    """Returns the details for a specific given video"""
    video = get_object_or_404(
        models.Video,
        video_id=video_id,
    )

    if not video.active or video.visibility == 'Private':
        raise PermissionDenied(detail={
            'video': 'Is not active or Private'
        })

    serializer = serializers.VideoSerializer(instance=video)
    return Response(serializer.data)


@api_view(['post'])
def search_videos(request, **kwargs):
    """Searches all the videos from the platform"""
    queryset = models.Video.objects.filter(
        active=True,
        visibility='Public'
    )
    serializer = serializers.SearchSerializer(
        instance=queryset,
        data=request.data
    )
    serializer.is_valid(raise_exception=True)
    return Response(serializer.search(request))


class ViewingProfile(APIView):
    serializer_class = serializers.ViewingProfileSerializer
    http_method_names = ['get', 'post']
    # authentication_classes = [IsAuthenticated]
    # permission_classes = []

    def get(self, request, **kwargs):
        profile = get_object_or_404(models.ViewingProfile, user=request.user)
        serializer = self.serializer_class(instance=profile)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        profile = get_object_or_404(models.ViewingProfile, user=request.user)
        serializer = serializers.ValidateViewingProfile(
            instance=profile,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = self.serializer_class(instance=profile)
        return Response(serializer.data)


class ListUserVideos(APIView):
    """Use this view for maniapulating data or actions
    on the `/my-studio` endpoint of the frontend"""

    http_method_names = ['get', 'post']
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = serializers.VideoSerializer

    def get(self, request, *args, **kwargs):
        videos = models.Video.objects.filter(user=request.user)
        serializer = self.serializer_class(instance=videos, many=True)
        return Response(serializer.data)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def upload_video(request, **kwargs):
    serializer = serializers.ValidateVideoUpload(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(request)
    return Response(serializer.data)
