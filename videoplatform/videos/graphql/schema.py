import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo
from videos.models import Video, Tag
from videos.graphql.types import VideoTagType, VideosType
from django.core.cache import cache


class VideosConnection(relay.Connection):
    class Meta:
        node = VideosType


class VideosQuery(graphene.ObjectType):
    all_videos = relay.ConnectionField(VideosConnection)
    video = graphene.Node.Field(VideosType)
    search_videos = DjangoFilterConnectionField(VideosType)
    all_tags = graphene.List(VideoTagType)

    def resolve_all_videos(root, info: GraphQLResolveInfo):
        return Video.objects.all()

    # def resolve_all_tags(root, info, **kwargs):
    #     return Tag.objects.all()
    
    # def resolve_search_videos(root, info, **kwargs):
    #     return VideosType.get_queryset(Video.objects.all(), info)
    
    # def resolve_video(root, info, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Video.objects.get(pk=id)
    #     return None
