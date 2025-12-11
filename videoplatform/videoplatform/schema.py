import graphene
from videos.schema import VideosQuery
from accounts.schema import AccountsQuery


class Query(VideosQuery, AccountsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
