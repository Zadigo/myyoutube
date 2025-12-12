import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from videos.models import Video, Tag


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
            'recording_date': ['exact', 'lt', 'gt'],
            'recording_language': ['exact'],
            'views': ['lte', 'gte'],
            'created_on': ['exact', 'lt', 'gt'],
            'tags__name': ['exact', 'icontains'],
            'user__username': ['exact', 'icontains'],
            'user_channel__name': ['exact', 'icontains'],
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        print(info)
        return queryset.filter(active=True, visibility='Public')


class VideosConnection(relay.Connection):
    class Meta:
        node = VideosType


class VideosQuery(graphene.ObjectType):
    video = graphene.Node.Field(VideosType)
    allvideos = relay.ConnectionField(VideosConnection)
    searchvideos = DjangoFilterConnectionField(VideosType)
    alltags = graphene.List(VideoTagType)

    def resolve_allvideos(self, info, **kwargs):
        return Video.objects.select_related('user', 'user_channel', 'channel_playlist').all()
