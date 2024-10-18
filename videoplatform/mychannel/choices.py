from django.db.models import Choices

class ChannelCategories(Choices):
    BEAUTY = 'Beauty'
    COMMENTARY = 'Commentary'
    CORPORATE = 'Corporate'
    OTHER = 'Other'
