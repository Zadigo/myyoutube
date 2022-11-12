from django.core.validators import FileExtensionValidator


def avatar_extension_validator(name):
    instance = FileExtensionValidator(['jpg', 'jpeg', 'png'])
    instance(name)
