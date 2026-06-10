from django.db.models import Choices, IntegerChoices


class AccountTypes(Choices):
    BASIC = 'Basic'
    ARTIST = 'Artist'
    PROFESSIONNAL = 'Professionnal'
    CORPORATE = 'Corporate'


class Performance(Choices):
    AUTO = 'Auto'
    P1080 = '1080p'
    P720 = '720p'


class SubscriptionChoice(IntegerChoices):
    FREE = 1, 'Free'
    MYVIDEO_PLUS = 2, 'My Video Plus'
    MYVIDEO_PLUS_PLUS = 3, 'My Video Plus Plus'
