import graphene
from django.core.cache import cache
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLFieldResolver, GraphQLResolveInfo
from playlists.models import Playlist
from playlists.graphql.types import PlaylistType 
from django.contrib.auth import get_user_model
from accounts.models import UserProfile, Subscription, PreferredAd, ViewingProfile, ActivationToken, CustomUser


class CustomUserType(DjangoObjectType):
    full_name = graphene.String(source='get_full_name')
    short_name = graphene.String(source='get_short_name')

    class Meta:
        model = CustomUser
        fields = '__all__'


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = '__all__'


class SubscriptionType(DjangoObjectType):
    class Meta:
        model = Subscription
        fields = '__all__'


class PreferredAdType(DjangoObjectType):
    class Meta:
        model = PreferredAd
        fields = '__all__'


class ViewingProfileType(DjangoObjectType):
    account_type = graphene.String()

    class Meta:
        model = ViewingProfile
        fields = '__all__'

    def resolve_account_type(self, info):
        return str(self.account_type)


class ActivationTokenType(DjangoObjectType):
    class Meta:
        model = ActivationToken
        fields = '__all__'
