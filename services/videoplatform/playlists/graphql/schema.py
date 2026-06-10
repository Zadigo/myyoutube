import graphene
from django.core.cache import cache
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLFieldResolver, GraphQLResolveInfo
from playlists.models import Playlist
from playlists.graphql.types import PlaylistType 

class PlaylistConnection(relay.Connection):
    class Meta:
        node = PlaylistType


class PlaylistQuery(graphene.ObjectType):
    playlist = graphene.Node.Field(PlaylistType)
    all_playlists = relay.ConnectionField(PlaylistConnection)
    search_playlists = DjangoFilterConnectionField(PlaylistType)

    def resolve_all_playlists(self, info: GraphQLResolveInfo, **kwargs):
        return Playlist.objects.all()
