import graphene
from accounts.schema import AccountsQuery
from videos.schema import VideosQuery
from mychannel.schema import MyChannelQuery
from playlists.schema import PlaylistQuery
from comments.schema import CommentsQuery


class Query(VideosQuery, AccountsQuery, MyChannelQuery, CommentsQuery, PlaylistQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
