import graphene
from graphene_django import DjangoObjectType
from playlists.models import Playlist
from django.core.cache import cache


class PlaylistType(DjangoObjectType):
    class Meta:
        model = Playlist
        fields = '__all__'

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related('user').prefetch_related('videos')


class PlaylistQuery(graphene.ObjectType):
    playlist = graphene.Field(PlaylistType, id=graphene.ID(required=True))
    allplaylists = graphene.List(PlaylistType)

    def resolve_playlist(self, info, id):
        return Playlist.objects.get(pk=id)

    def resolve_allplaylists(self, info):
        return Playlist.objects.all()
