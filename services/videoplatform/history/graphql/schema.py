import graphene
from graphene import relay
from graphql import GraphQLResolveInfo

from history.graphql.types import HistoryType
from history.models import History
from typing import Optional

class HistoryConnection(relay.Connection):
    class Meta:
        node = HistoryType
    

class HistoryQuery(graphene.ObjectType):
    all_history = relay.ConnectionField(HistoryConnection)
    search_history = relay.ConnectionField(HistoryConnection, search=graphene.String())

    def resolve_all_history(root, info: GraphQLResolveInfo):
        return History.objects.all()

    def resolve_search_history(root, info: GraphQLResolveInfo, search: Optional[str] = None):
        queryset = History.objects.all()
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
