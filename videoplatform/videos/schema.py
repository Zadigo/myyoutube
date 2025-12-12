import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from videos.models import Video


class VideosNode(DjangoObjectType):
    class Meta:
        model = Video
        interfaces = (relay.Node,)
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['icontains'],
            'video_id': ['exact']
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        print(info)
        return queryset.filter(active=True, visibility='Public')


class VideosConnection(relay.Connection):
    class Meta:
        node = VideosNode


class VideosQuery(graphene.ObjectType):
    video = graphene.Node.Field(VideosNode)
    # allvideos = DjangoFilterConnectionField(VideosNode)
    allvideos = relay.ConnectionField(VideosConnection)
    searchvideos = DjangoFilterConnectionField(VideosNode)

    def resolve_allvideos(self, info, **kwargs):
        return Video.objects.select_related('user', 'user_channel', 'channel_playlist').all()
