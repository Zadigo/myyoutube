import pathlib

from comments.models import Comment
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.serializers import serialize
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


class TestCommentApi(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    def setUp(self):
        self.video = Video.objects.first()

        comments = [
            {
                'user': self.user,
                'video': self.video,
                'content': 'Text 1'
            },
            {
                'user': self.user,
                'video': self.video,
                'content': 'Text 2'
            }
        ]

        for comment in comments:
            Comment.objects.create(**comment)

    def test_list_comments(self):
        path = reverse(
            'comments_api:list_comments',
            args=[self.video.video_id]
        )
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('user', data[0])
