import json
import secrets
from django.core.exceptions import ValidationError


def stories_directory_path(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(5)}.{extension}'
    return f'uploads/stories/{instance.user.userchannel_set.get().reference}/{new_file_name}'


def video_directory_path(instance, filename):
    """Uploads a video directly to the path that
    this specific function directs it to"""
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(15)}.{extension}'
    try:
        channel_reference = instance.user.userchannel_set.get().reference
    except:
        raise ValidationError(
            message=(
                "Trying to upload a video without a channel "
                "is not authorized"
            )
        )
    else:
        return f'uploads/{channel_reference}/{new_file_name}'


def vue_dict(item):
    return json.dumps(item)
