from django.db.models import Choices


class RatingTypes(Choices):
    LIKE = 'Like'
    DISLIKE = 'Dislike'


class RatingFor(Choices):
    COMMENT = 'Comment'
    REPLY = 'Reply'


class SubscriptionModes(Choices):
    ALL = 'All'
    IMPORTANT = 'Important'
    NONE = 'None'
