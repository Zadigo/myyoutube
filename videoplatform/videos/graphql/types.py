import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo
from videos.models import Video, Tag
from django.db.models import QuerySet


class VideoTagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = '__all__'


class VideosType(DjangoObjectType):
    class Meta:
        model = Video
        interfaces = (relay.Node,)
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['icontains'],
            'video_id': ['exact'],
            'age_restricted': ['exact'],
            'category': ['exact'],
            'visibility': ['exact'],
            'recording_date': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'recording_language': ['exact'],
            'views': ['lte', 'gte'],
            'created_on': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'tags__name': ['exact', 'icontains'],
            'user__username': ['exact', 'icontains'],
            'user_channel__name': ['exact', 'icontains'],
        }

    @classmethod
    def get_queryset(cls, queryset: QuerySet[Video], info: GraphQLResolveInfo):
        qs = queryset.select_related('user', 'user_channel', 'channel_playlist')
        return qs.filter(active=True, visibility='Public')

