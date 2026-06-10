import graphene
from graphene_django import DjangoObjectType
from ratings.models import Rating

class RatingEnums(graphene.Enum):
    LIKE = 'Like'
    DISLIKE = 'Dislike'


class RatingsType(DjangoObjectType):
    class Meta:
        model = Rating
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'user': ['exact'],
            'video__title': ['exact', 'icontains', 'istartswith'],
            'comment': ['exact'],
            'reply': ['exact'],
            'rating_for': ['exact'],
            'rating_type': ['exact'],
            'created_on': ['exact', 'lte', 'gte']
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return super().get_queryset(queryset, info)
