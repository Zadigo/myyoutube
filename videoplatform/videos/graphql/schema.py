import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo
from videos.models import Video, Tag
from videos.graphql.types import VideoTagType, VideosType
from django.core.cache import cache
import pydantic
import django_filters
from django.db.models import QuerySet
from typing import Optional
from django.core.cache import cache
from django.utils.timezone import now
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractWeek,
                                        ExtractYear, Now)

class VideosConnection(relay.Connection):
    class Meta:
        node = VideosType


class VideosFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr=['exact', 'icontains', 'istartswith'])
    this_month = django_filters.BooleanFilter(lookup_expr=['eq'], method='filter_this_month')
    this_year = django_filters.BooleanFilter(lookup_expr=['eq'], method='filter_this_year')
    last_week = django_filters.BooleanFilter(lookup_expr=['eq'], method='filter_last_week')
    today = django_filters.BooleanFilter(lookup_expr=['eq'], method='filter_today')

    class Meta:
        model = Video
        fields = ['title', 'recording_date']

    def filter_this_month(self, queryset: QuerySet[Video], name: str, value: bool):
        current_date = now()
        if value:
            return queryset.filter(
                recording_date__month=current_date.month,
                recording_date__year=current_date.year
            )
        return queryset
    
    def filter_this_year(self, queryset: QuerySet[Video], name: str, value: bool):
        current_date = now()
        if value:
            return queryset.filter(
                recording_date__year=current_date.year
            )
        return queryset
    
    def filter_last_week(self, queryset: QuerySet[Video], name: str, value: bool):
        current_date = now()
        if value:
            current_week = current_date.isocalendar().week
            return queryset.filter(
                recording_date__week=current_week - 1,
                recording_date__year=current_date.year
            )
        return queryset
    
    def filter_today(self, queryset: QuerySet[Video], name: str, value: bool):
        if value:
            return queryset.filter(created_on__date=Now())
        return queryset


class VideosQuery(graphene.ObjectType):
    all_videos = relay.ConnectionField(VideosConnection)
    video = graphene.Node.Field(VideosType)
    # search_videos = DjangoFilterConnectionField(VideosType, filterset_class=VideosFilterSet)
    search_videos = DjangoFilterConnectionField(VideosType)
    all_tags = graphene.List(VideoTagType)

    def resolve_all_videos(root, info: GraphQLResolveInfo):
        return Video.objects.all()
    
    # def resolve_search_videos(root, info: GraphQLResolveInfo, **kwargs):
    #     queryset = Video.objects.all()
    #     print(kwargs)
    #     return queryset

    # def resolve_all_tags(root, info, **kwargs):
    #     return Tag.objects.all()
    
    # def resolve_search_videos(root, info, **kwargs):
    #     return VideosType.get_queryset(Video.objects.all(), info)
    
    # def resolve_video(root, info, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Video.objects.get(pk=id)
    #     return None
