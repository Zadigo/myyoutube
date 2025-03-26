from datetime import timedelta
from django.utils import timezone
import json
import os
import pathlib
import re
from functools import lru_cache
from pathlib import Path
from wsgiref.util import FileWrapper

import pandas
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.models import BooleanField, Case, Q, When
from django.db.models.functions import StrIndex
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404
from mychannel.models import BlockedChannel
from rest_framework import generics, status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.exceptions import (AuthenticationFailed, NotFound,
                                       PermissionDenied)
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet
from videos import models
from videos.api import serializers


@lru_cache(maxsize=10)
def read_category_file():
    categories = cache.get('categories', default=[])
    if not categories:
        media_path = settings.MEDIA_ROOT.joinpath('sub_categories.json')
        with open(media_path, mode='r', encoding='utf-8') as f:
            categories = json.load(f)
    return categories


class ListVideoCategories(GenericViewSet):
    http_method_names = ['get']
    serializer_class = serializers.SubcategoriesSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        data = list(map(lambda x: {'title': x}, self.get_queryset()))

        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data)

    def get_queryset(self):
        data = read_category_file()
        return list(data.keys())


class ListVideoSubcategories(GenericViewSet):
    """Returns all the sub-categories for a given
    category in order to correctly classify a video
    on the platform
    """

    http_method_names = ['get']
    lookup_field = 'category'
    lookup_url_kwarg = 'category'
    permission_classes = []
    serializer_class = serializers.SubcategoriesSerializer
    error = 'Category is not valid'

    def list(self, request, *args, **kwargs):
        sub_categories = self.get_object()

        serializer = self.serializer_class(data=sub_categories, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)

    def get_queryset(self):
        categories = cache.get('categories', default=[])
        if not categories:
            media_path = settings.MEDIA_ROOT.joinpath('sub_categories.json')
            with open(media_path, mode='r', encoding='utf-8') as f:
                categories = json.load(f)
                cache.set('categories', categories, timeout=3600)
        return categories

    def get_object(self):
        categories = self.get_queryset()

        category_name = self.kwargs[self.lookup_url_kwarg]
        sub_category = cache.get(category_name, default=[])
        if not sub_category:
            sub_category = categories.get(category_name)
            if sub_category is None:
                raise ValidationError(self.error)

        cache.set(self.lookup_url_kwarg, sub_category, timeout=3600)
        df = pandas.DataFrame({'title': sub_category})
        data = json.loads(df.to_json(orient='records', force_ascii=False))
        return data


class ListVideos(ListAPIView):
    queryset = models.Video.objects.filter(active=True, visibility='Public')
    serializer_class = serializers.VideoSerializer
    pagination_class = None
    permission_classes = []

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            # 1. Remove all the videos that contains
            # a channel that was blocked by the
            # current user
            cache_key = f'blocked_channels_user_{self.request.user.id}'
            blocked_channels = cache.get(cache_key, None)
            if blocked_channels is None:
                blocked_channels = BlockedChannel.objects.filter(
                    user=self.request.user
                )
                cache.set(cache_key, qs, timeout=1)

            if blocked_channels.exists():
                blocked_ids = blocked_channels.values_list('id', flat=True)
                qs = queryset.exclude(user_channel__in=blocked_ids)

            # 2. Get the blocked keywords that the user
            # has specified an if they are present in
            # in the videos description, title and hashtags
            # then the video has to be excluded
            # logic = (
            #     Q(title=StrIndex())
            # )
            # condition = When(logic, then=True)
            # case = Case(condition, default=False, output_field=BooleanField())
            # qs2 = queryset.annotate(has_blocked_keywords=case)
            # queryset = qs2.filter(has_blocked_keywords=False)

        return qs


class UploadVideo(CreateModelMixin, GenericAPIView):
    queryset = None
    http_method_names = ['post']
    serializer_class = serializers.ValidateVideoUpload
    permission_classes = [IsAuthenticated]


class GetVideo(RetrieveAPIView):
    queryset = models.Video.objects.filter(active=True)
    serializer_class = serializers.VideoSerializer
    permission_classes = []
    lookup_field = 'video_id'
    lookup_url_kwarg = 'video_id'

    def get_queryset(self):
        qs = cache.get('active_videos_public', None)
        if qs is None:
            qs = super().get_queryset()
            cache.set('active_videos_public', qs, timeout=1)
            return qs.filter(visibility='Public')
        return qs

    def get_object(self):
        video = super().get_object()
        if not video.active or video.visibility == 'Private':
            raise PermissionDenied(
                **{
                    'detail': {
                        'video': 'Is not active or Private'
                    }
                }
            )
        return video


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


class UploadVideo(generics.GenericAPIView):
    serializer_class = serializers.ValidateVideoUpload
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return_serializer = serializers.VideoSerializer(
            instance=serializer.instance
        )
        return Response(data=return_serializer.data, status=status.HTTP_201_CREATED)


class VideoStreamView(APIView):
    """Endpoint used to stream an uploaded video
    to the frontend without loading the full content
    in memory"""

    def get(self, request, video_id):
        video = get_object_or_404(
            models.Video,
            video_id=video_id,
        )

        if video.video.path is None:
            raise NotFound(detail='Video not found')

        video_path = pathlib.Path(video.video.path)

        # Check if the video file exists
        if not video_path.exists():
            raise NotFound(detail='Video not found')

        video_size = os.path.getsize(video_path)
        range_header = request.headers.get('Range', None)

        # If no Range header, return the whole video
        if range_header is None:
            response = StreamingHttpResponse(
                open(video_path, 'rb'),
                content_type='video/mp4'
            )
            response['Content-Length'] = str(video_size)
            return response

        # Handle Range request (partial content)
        range_match = re.match(r'bytes=(\d+)-(\d+)?', range_header)
        if range_match:
            start = int(range_match.group(1))
            end = range_match.group(2)
            if end is not None:
                end = int(end)
            else:
                end = video_size - 1
        else:
            return Response(status=416)  # Range Not Satisfiable

        # Prepare response for partial content
        response = StreamingHttpResponse(
            open(video_path, 'rb'),
            content_type='video/mp4',
            status=206
        )
        response['Content-Length'] = str(end - start + 1)
        response['Content-Range'] = f'bytes {start}-{end}/{video_size}'

        # Seek to the start byte in the file
        video_file = open(video_path, 'rb')
        video_file.seek(start)
        response.streaming_content = iter(lambda: video_file.read(8192), b'')

        return response


class CreateCommentAPI(GenericAPIView):
    """Endpoint used to create a new
    comment on a given video"""

    serializer_class = CommentSerializer
    queryset = models.Video.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'video_id'
    lookup_url_kwarg = 'video_id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['video'] = self.get_object()
        return context

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = self.get_object()
        comment = serializer.save()

        if request.user == video.user:
            comment.from_creator = True
            comment.save()

        # notification = Notification.objects.create()
        return Response(serializer.data)


class FeedBuilderEndpoint(GenericAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializers.ValidateFeedBuilderSerializer
    permission_classes = []

    def get_queryset(self, filters):
        qs = super().get_queryset()
        last_seven_days = timezone.now() - timedelta(days=7)
        qs = qs.filter(created_on__gte=last_seven_days)
        return qs.order_by('-created_on')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        filters = serializer.data
        qs = self.get_queryset(filters)

        serializer = serializers.VideoFeedBuilderSerialier(
            instance=qs,
            many=True
        )
        return Response(serializer.data)
