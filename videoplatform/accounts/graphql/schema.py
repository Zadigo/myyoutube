import graphene
from django.core.cache import cache
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLFieldResolver, GraphQLResolveInfo
from playlists.models import Playlist
from playlists.graphql.types import PlaylistType 
from django.contrib.auth import get_user_model
from accounts.models import UserProfile, Subscription, PreferredAd, ViewingProfile, ActivationToken
from accounts.graphql.types import CustomUserType, UserProfileType, SubscriptionType, PreferredAdType, ViewingProfileType, ActivationTokenType

class CustomUserQuery(graphene.ObjectType):
    get_user = graphene.Field(CustomUserType, id=graphene.String(required=True))

    def resolve_get_user(self, info, id):
        try:
            return get_user_model().objects.get(pk=id)
        except get_user_model().DoesNotExist:
            return None


class UserProfileQuery(graphene.ObjectType):
    all_user_profiles = graphene.List(UserProfileType)

    def resolve_all_user_profiles(self, info):
        return UserProfile.objects.all()


class SubscriptionQuery(graphene.ObjectType):
    all_subscriptions = graphene.List(SubscriptionType)

    def resolve_all_subscriptions(self, info):
        return Subscription.objects.all()


class PreferredAdQuery(graphene.ObjectType):
    all_preferred_ads = graphene.List(PreferredAdType)

    def resolve_all_preferred_ads(self, info):
        return PreferredAd.objects.all()


class ViewingProfileQuery(graphene.ObjectType):
    all_viewing_profiles = graphene.List(ViewingProfileType)
    get_viewing_profile = graphene.Field(ViewingProfileType, id=graphene.String(required=True))

    def resolve_all_viewing_profiles(self, info):
        return ViewingProfile.objects.all()
    
    def resolve_get_viewing_profile(self, info: GraphQLResolveInfo, id: str):
        try:
            return ViewingProfile.objects.get(pk=id)
        except ViewingProfile.DoesNotExist:
            return None


class ActivationTokenQuery(graphene.ObjectType):
    all_activation_tokens = graphene.List(ActivationTokenType)

    def resolve_all_activation_tokens(self, info):
        return ActivationToken.objects.all()
