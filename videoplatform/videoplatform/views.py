from asgiref.sync import async_to_sync
from django.utils.crypto import get_random_string, salted_hmac
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import Response

from videoplatform.utils import get_firebase_app


class ViewingProfileToken(GenericAPIView):
    """An endpoint that creates a new vienwing profile
    in Firebase. A viewing profile can be considered as
    storage that includes all the viewing data for a given
    user in a real-time database"""

    default_collection = 'vp_profiles'

    @property
    def default_viewing_profile(self):
        template = {
            'id': None,
            'email': None
        }

        if self.request.user.is_authenticated:
            template['id'] = self.request.user.id,
            template['email'] = self.request.user.email
        return template

    def _transform(self, user_id: int, email: str):
        return

    def post(self, request, **kwargs):
        template = {'token': None}
        if request.user.is_authenticated:
            template['token'] = f'vp_{get_random_string(length=20)}'
        template['token'] = f'vp_{get_random_string(length=20)}'

        db = get_firebase_app()
        task = db.collection(self.default_collection)
        async_to_sync(task.document(template['token']).set)(
            self.default_viewing_profile
        )
        return Response(template)
