import graphene
from django.core.cache import cache
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLResolveInfo
from playlists.models import Playlist
from django.db.models import QuerySet


class PlaylistType(DjangoObjectType):
    class Meta:
        model = Playlist
        interfaces = (relay.Node,)
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'description': ['icontains'],
            'visibility': ['exact'],
            'is_intelligent': ['exact'],
            'created_on': ['exact', 'lt', 'gt'],
        }

    @classmethod
    def get_queryset(cls, queryset: QuerySet[Playlist], info: GraphQLResolveInfo):
        return queryset.select_related('user').all()

