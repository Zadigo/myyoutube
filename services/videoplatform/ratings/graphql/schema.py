import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphql import GraphQLResolveInfo
from ratings.models import Rating

from ratings.graphql.types import RatingsType


class RatingsTypeConnection(relay.Connection):
    class Meta:
        node = RatingsType


class RatingsQuery(graphene.ObjectType):
    all_ratings = relay.ConnectionField(RatingsTypeConnection)

    def resolve_all_ratings(self, info: GraphQLResolveInfo):
        print(info.context)
        return Rating.objects.all()
