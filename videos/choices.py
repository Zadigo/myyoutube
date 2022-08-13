from django.db.models import Choices

class VisibilityChoices(Choices):
    PUBLIC = 'Public'
    PRIVATE = 'Private'


class CategoryChoices(Choices):
    FILM_AND_ANIMATION = 'Film and animation'
    MUSIC = 'Music'
    GAMING = 'Gaming'
    ENTERTAINMENT = 'Entertainment'
    FASHION = 'Fashion'
    BEAUTY = 'Beauty'


class LanguageChoices(Choices):
    FRENCH = 'French'
    ENGLISH = 'English'


class CommentingStrategy(Choices):
    ALLOW_ALL_COMMENTS = 'Allow all comments'
    HOLD_FOR_REVIEW = 'Hold all comments for review'
    DISABLE_ALL = 'Disable all comments'
