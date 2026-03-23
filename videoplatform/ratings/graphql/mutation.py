import graphene
import graphene_django
from ratings.models import Rating
from django.shortcuts import get_object_or_404
from ratings.graphql.types import RatingEnums

class CreateRatingMutation(graphene.Mutation):
    class Arguments:
        video_id = graphene.ID(required=True)
        rating = RatingEnums()

    success = graphene.Boolean()

    def mutate(self, info: graphene.ResolveInfo, video_id: str, rating: str):
        if info.context.user.is_anonymous:
            raise Exception('Authentication required to rate a video.')
        
        rating_type = RatingEnums.LIKE if rating == 'Like' else RatingEnums.DISLIKE
        qs = Rating.objects.filter(
            video_id=video_id, 
            user=info.context.user,
            rating_type=rating_type
        )
        
        if qs.exists():
            return CreateRatingMutation(success=False)
        
        instance = qs.first()
        if instance is not None:
            instance.rating_type = rating_type
            instance.save()
        return CreateRatingMutation(success=True)
