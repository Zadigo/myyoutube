import graphene
from videos.graphql.utils import VisibilityEnum
from playlists.graphql.types import PlaylistType
from playlists.models import Playlist

class CreatePlaylistMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        visibility = VisibilityEnum()
        is_intelligent = graphene.Boolean()

    playlist = graphene.Field(PlaylistType)

    def mutate(self, info, name, visibility, description=None, is_intelligent=False):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required to create a playlist.")
        
        playlist = Playlist.objects.create(
            user=user,
            name=name,
            description=description,
            visibility=visibility,
            is_intelligent=is_intelligent
        )
        return CreatePlaylistMutation(playlist=playlist)
