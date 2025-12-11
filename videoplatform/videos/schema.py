import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from videos.models import Video


class VideosNode(DjangoObjectType):
    class Meta:
        model = Video
        interfaces = (relay.Node,)
        filter_fields = {}


class SearchByNode(DjangoObjectType):
    class Meta:
        model = Video
        interfaces = (relay.Node,)
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['icontains'],
            'video_id': ['exact']
        }


class VideosQuery(graphene.ObjectType):
    video = graphene.Node.Field(SearchByNode)
    allvideos = DjangoFilterConnectionField(VideosNode)
    searchvideos = DjangoFilterConnectionField(SearchByNode)
