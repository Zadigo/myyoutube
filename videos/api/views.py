from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from videos import models, serializers
from videos.choices import VisibilityChoices


@api_view(['post'])
def get_videos(request, **kwargs):
    """Returns all the videos from the plateform"""
    queryset = models.Video.objects.all()
    serializer = serializers.VideoSerializer(instance=queryset, many=True)
    return Response(serializer.data)


@api_view(['post'])
def get_video(request, reference, **kwargs):
    """Returns the details for a specific given video"""
    video = get_object_or_404(models.Video, reference=reference)
    serializer = serializers.VideoSerializer(instance=video)
    return Response(serializer.data)


@api_view(['post'])
def search_videos(request, **kwargs):
    queryset = models.Video.objects.active_videos()
    serializer = serializers.SearchSerializer(
        instance=queryset, data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.search(request)
    return Response(data)


class ViewingProfile(APIView):
    serializer_class = serializers.ViewingProfileSerializer
    http_method_names = ['get', 'post']
    permission_classes = []

    def get(self, request, **kwargs):
        profile = get_object_or_404(models.ViewingProfile, user=request.user)
        serializer = self.serializer_class(instance=profile)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        profile = get_object_or_404(models.ViewingProfile, user=request.user)
        serializer = serializers.ValidateUpdateViewingProfile(
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
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.VideoSerializer

    def get(self, request, *args, **kwargs):
        videos = models.Video.objects.filter(user=request.user)
        serializer = self.serializer_class(instance=videos, many=True)
        return Response(serializer.data)
