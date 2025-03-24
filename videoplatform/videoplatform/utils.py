import firebase_admin
from firebase_admin.credentials import ApplicationDefault
from django.conf import settings
from django.utils.crypto import get_random_string
from rest_framework.pagination import LimitOffsetPagination
from firebase_admin import firestore_async


def create_id(prefix, k=15):
    """Creates a usable database reference ID"""
    return f'{prefix}_{get_random_string(length=k)}'


class CustomPagination(LimitOffsetPagination):
    max_limit = 100


def get_firebase_app():
    credentials = ApplicationDefault()
    app = firebase_admin.initialize_app(
        credential=credentials, 
        options={
            'projectId': getattr(settings, 'FIREBASE_PROJECT_ID')
        }
    )
    return firestore_async.client()
