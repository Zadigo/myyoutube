from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse
from history import tasks
from rest_framework.test import APITestCase
from videos.models import Video


class AuthenticationMixin(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.first()
        cls.user.set_password('touparet')
        cls.user.save()

    def setUp(self):
        self.client = self.client_class()
        self.token = self._authenticate()

    def _authenticate(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'email': self.user.email,
                'password': 'touparet'
            }
        )

        self.assertEqual(response.status_code, 200, 'Authentication failed')

        token = response.json().get('access')
        self.assertIsNotNone(token, 'Token retrieval failed')

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        return token


@override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPAGATES=True)
class TestTasks(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    def test_add_video_to_history(self):
        video = Video.objects.first()
        t1 = tasks.add_video_to_history.apply(
            (
                video.id,
                self.user.id
            )
        )
        result = t1.get()
