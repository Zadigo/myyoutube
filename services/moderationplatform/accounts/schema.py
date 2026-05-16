import graphene
from django.contrib.auth import get_user_model
from graphene import relay
from graphene_django import DjangoObjectType


class AuthorType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'date_joined']


class AccountsQuery(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.ID(required=True))

    def resolve_all_authors(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_author(self, info, id):
        return get_user_model().objects.get(id=id)
