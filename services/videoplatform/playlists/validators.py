from rest_framework.exceptions import ValidationError

def validate_description(text):
    if len(text) < 30 and len(text) > 200:
        raise ValidationError(detail={
            'description': 'Description is not valid'
        })
