import graphene
from accounts.schema import AccountsQuery
# from videos.schema import VideosQuery
from videos.graphql.schema import VideosQuery
from mychannel.schema import MyChannelQuery
from playlists.schema import PlaylistQuery
from comments.schema import CommentsQuery
from videos.graphql.mutation import CreateVideoMutation
from playlists.graphql.mutation import CreatePlaylistMutation
from ratings.graphql.mutation import CreateRatingMutation

class Query(
    VideosQuery, 
    AccountsQuery, 
    MyChannelQuery, 
    CommentsQuery, 
    PlaylistQuery, 
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_video = CreateVideoMutation.Field()
    create_playlist = CreatePlaylistMutation.Field()
    create_rating = CreateRatingMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
