from django.db.models import Choices

class RatingTypes(Choices):
    LIKE = 'Like'
    DISLIKE = 'Dislike'


class RatingFor(Choices):
    COMMENT = 'Comment'
    VIDEO = 'Video'
    REPLY = 'Reply'
    