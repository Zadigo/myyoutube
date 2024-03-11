from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def donation_validator(value):
    if value < 5:
        raise ValidationError(_('Donation value should be above 5'))

    if value > 500:
        raise ValidationError(_('Donation value cannot be above 500'))
    
    return value
