from django.utils.crypto import get_random_string


def create_id(prefix, k=15):
    """Creates a usable database reference ID"""
    return f'{prefix}_{get_random_string(length=k)}'
