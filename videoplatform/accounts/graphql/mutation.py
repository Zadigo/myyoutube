from typing import Optional

import graphene
from graphql import GraphQLResolveInfo
from videos.graphql.utils import VisibilityEnum
from accounts.graphql.types import ViewingProfileType
from accounts.models import ViewingProfile

class UpdateViewingProfileMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        night_mode = graphene.Boolean(required=False)
        algorithm_decides = graphene.Boolean(required=False)
        recommend_popular_videos = graphene.Boolean(required=False)
        # blocked_keywords = graphene.List(graphene.JSONString, required=False)
        subscriptions_private = graphene.Boolean(required=False)
        personalize_ads = graphene.Boolean(required=False)

    viewing_profile = graphene.Field(ViewingProfileType)

    @classmethod
    def mutate(cls, root, info: GraphQLResolveInfo, id: str, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception("Authentication required")
        
        try:
            viewing_profile = ViewingProfile.objects.get(pk=id)
        except ViewingProfile.DoesNotExist:
            raise Exception("Viewing profile not found")

        night_mode = kwargs.get('night_mode', False)
        if night_mode is not None:
            viewing_profile.night_mode = night_mode

        algorithm_decides = kwargs.get('algorithm_decides', False)
        if algorithm_decides is not None:
            viewing_profile.algorithm_decides = algorithm_decides

        recommend_popular_videos = kwargs.get('recommend_popular_videos', False)
        if recommend_popular_videos is not None:
            viewing_profile.recommend_popular_videos = recommend_popular_videos

        subscriptions_private = kwargs.get('subscriptions_private', False)
        if subscriptions_private is not None:
            viewing_profile.subscriptions_private = subscriptions_private

        personalize_ads = kwargs.get('personalize_ads', False)
        if personalize_ads is not None:
            viewing_profile.personalize_ads = personalize_ads

        viewing_profile.save()
        return UpdateViewingProfileMutation(viewing_profile=viewing_profile)
