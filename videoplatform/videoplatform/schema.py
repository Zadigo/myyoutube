import graphene
from accounts.schema import AccountsQuery
from videos.graphql.schema import VideosQuery
from playlists.schema import PlaylistQuery
from mychannel.graphql.schema import MyChannelQuery
from videos.graphql.mutation import CreateVideoMutation
from playlists.graphql.mutation import CreatePlaylistMutation
from ratings.graphql.mutation import CreateRatingMutation
from ratings.graphql.schema import RatingsQuery


class Query(
    VideosQuery,
    AccountsQuery,
    MyChannelQuery,
    PlaylistQuery,
    RatingsQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_video = CreateVideoMutation.Field()
    create_playlist = CreatePlaylistMutation.Field()
    create_rating = CreateRatingMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
