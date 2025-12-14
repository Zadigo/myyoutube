import graphene
from graphene_django import DjangoObjectType
from reportsources.models import ReportSource


class ReportSourceType(DjangoObjectType):
    class Meta:
        model = ReportSource
        fields = '__all__'


class ReportSourceQuery(graphene.ObjectType):
    allsources = graphene.List(ReportSourceType)

    def resolve_allsources(self, info, **kwargs):
        return ReportSource.objects.all()
