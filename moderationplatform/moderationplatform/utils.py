from django.utils.crypto import get_random_string
from rest_framework.pagination import LimitOffsetPagination


def create_id(prefix, k=15):
    """Creates a usable database reference ID"""
    return f'{prefix}_{get_random_string(length=k)}'


class CustomPagination(LimitOffsetPagination):
    max_limit = 100
