import graphene
from accounts.schema import AccountsQuery
from videos.schema import VideosQuery
from mychannel.schema import MyChannelQuery


class Query(VideosQuery, AccountsQuery, MyChannelQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
