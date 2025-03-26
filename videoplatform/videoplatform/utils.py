import os

# import firebase_admin
# from django.conf import settings
from django.utils.crypto import get_random_string
# from firebase_admin import firestore_async
# from firebase_admin.credentials import ApplicationDefault
from rest_framework.pagination import LimitOffsetPagination

# credentials = ApplicationDefault()
# app = firebase_admin.initialize_app(
#     credential=credentials,
#     options={
#         'projectId': getattr(settings, 'FIREBASE_PROJECT_ID')
#     }
# )


def create_id(prefix, k=15):
    """Creates a usable database reference ID"""
    return f'{prefix}_{get_random_string(length=k)}'


class CustomPagination(LimitOffsetPagination):
    max_limit = 100


# def get_firebase_app():
#     return firestore_async.client()
