import graphene
from ratings.graphql.utils import RatingTypes
from ratings.models import Rating

class CreateRatingMutation(graphene.Mutation):
    class Arguments:
        video_id = graphene.ID(required=True)
        rating = RatingTypes(required=True)

    success = graphene.Boolean()

    def mutate(self, info: graphene.ResolveInfo, video_id, rating):
        if info.context.user.is_anonymous:
            raise Exception('Authentication required to rate a video.')
        
        instance = Rating.objects.get(video_id=video_id, user=info.context.user)
        instance.rating = rating
        instance.save()
        return CreateRatingMutation(success=True)
