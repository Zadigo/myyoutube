import graphene

class VisibilityEnum(graphene.Enum):
    PUBLIC = 'Public'
    PRIVATE = 'Private'

class CategoryEnum(graphene.Enum):
    FILM_AND_ANIMATION = 'Film and animation'
    MUSIC = 'Music'
    GAMING = 'Gaming'
    ENTERTAINMENT = 'Entertainment'
    FASHION = 'Fashion'
    BEAUTY = 'Beauty'


class CommentingStrategyEnum(graphene.Enum):
    ALLOW_ALL_COMMENTS = 'Allow all comments'
    HOLD_FOR_REVIEW = 'Hold all comments for review'
    DISABLE_ALL = 'Disable all comments'
