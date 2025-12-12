import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from accounts.models import CustomUser, UserProfile, Subscription


class CustomUserNode(DjangoObjectType):
    class Meta:
        model = CustomUser
        interfaces = (relay.Node,)
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith']
        }


class UserProfileNode(DjangoObjectType):
    class Meta:
        model = UserProfile
        interfaces = (relay.Node,)
        # convert_choices_to_enum = ['subscription']
        filter_fields = {
            'city': ['exact', 'icontains', 'istartswith'],
            # 'subscription': ['exact', 'icontains']
        }


class AccountsQuery(graphene.ObjectType):
    user = graphene.Node.Field(CustomUserNode)
    allusers = DjangoFilterConnectionField(CustomUserNode)

    userprofile = graphene.Node.Field(UserProfileNode)
    alluserprofiles = DjangoFilterConnectionField(UserProfileNode)
