from django.utils.crypto import get_random_string


def avatar_path(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{get_random_string(length=30)}.{extension}'
    return f'avatars/user_{instance.user.id}/{new_file_name}'
