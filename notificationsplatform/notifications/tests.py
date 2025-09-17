from django.test import TransactionTestCase, override_settings
from notifications import tasks
from videos.models import Video
from rest_framework.test import APITestCase


from django.contrib.auth import get_user_model
from django.test import TransactionTestCase, override_settings
from django.urls import reverse
from rest_framework.test import APITestCase
from videos import tasks
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


class TestNotificationApi(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    def test_get_notification_profile(self):
        path = reverse('notifications_api:detail')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_update_notification_profile(self):
        path = reverse('notifications_api:detail')
        data = {
            'subscribed_channel_activity': True,
            'video_recommendation': True,
            'channel_activity': True,
            'replies_activity': True,
            'mentions': True,
            'repost': True
        }
        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, 200)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPAGATES=True)
class TestTasks(TransactionTestCase):
    fixtures = ['videos']

    def test_add_notification(self):
        video = Video.objects.first()

        t1 = tasks.add_notiication.apply(args=(
            video.user.id,
            video.id,
            'Message'
        ))
        result = t1.get()
