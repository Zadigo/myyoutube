from graphene_django import DjangoObjectType
from graphql import GraphQLResolveInfo
from history.models import History
from django.db.models import QuerySet


class HistoryType(DjangoObjectType):
    class Meta:
        model = History
        fields = '__all__'

    @classmethod
    def get_queryset(cls, queryset: QuerySet[History], info: GraphQLResolveInfo):
        qs = queryset.select_related('user', 'video')
        return qs.filter(user=info.context.user, active=True)

