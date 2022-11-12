from django.core.exceptions import ValidationError


def donation_validator(value):
    if value < 5:
        raise ValidationError('The donation value should be above 5')

    if value > 500:
        raise ValidationError('The donation value cannot be above 500')
    
    return value
