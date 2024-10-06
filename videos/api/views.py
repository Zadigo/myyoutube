import json
from functools import lru_cache

import pandas
from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db.models import BooleanField, Case, Q, When
from django.db.models.functions import StrIndex
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from mychannel.models import BlockedChannel
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


class ListVideos(ListModelMixin, GenericAPIView):
    http_method_names = ['post']
    serializer_class = serializers.VideoSerializer
    pagination_class = None
    queryset = models.Video.objects.filter(active=True, visibility='Public')
    permission_classes = []

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(instance=queryset, many=True)
        return Response(serializer.data)

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            # 1. Remove all the videos that contains
            # a channel that was blocked by the
            # current user
            blocked_channels = BlockedChannel.objects.filter(
                user=self.request.user
            )
            if blocked_channels.exists():
                queryset = queryset.exclude(
                    video__user_channel__in=blocked_channels
                )

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

        return queryset


class UploadVideo(CreateModelMixin, GenericAPIView):
    queryset = None
    http_method_names = ['post']
    serializer_class = serializers.ValidateVideoUpload
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request)


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
    video = serializer.save(request)
    return_serializer = serializers.VideoSerializer(instance=video)
    return Response(return_serializer.data)
