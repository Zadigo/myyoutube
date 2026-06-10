from django.core.validators import FileExtensionValidator
from rest_framework.exceptions import ValidationError


def validate_keywords(value):
    pass


def validate_video_title(title):
    if len(title) < 10:
        raise ValidationError('Title should be at least 10 caracters')


def validate_file(file):
    validator = FileExtensionValidator(allowed_extensions=['mp4'])
    validator(file)

    # 10GB * 1024
    max_size = 10 * 2**30
    if file.size > max_size:
        raise ValidationError('File size error')
