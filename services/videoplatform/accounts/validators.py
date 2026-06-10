import datetime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


def avatar_extension_validator(name):
    instance = FileExtensionValidator(['jpg', 'jpeg', 'png'])
    instance(name)


def birthdate_validator(value):
    year_limit = datetime.datetime.now().year - 18
    if value.year > year_limit:
        raise ValidationError('Age not valid')
