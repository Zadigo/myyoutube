import pathlib
from unittest import TestCase, IsolatedAsyncioTestCase

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


class TestVideoApiResponse(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    @classmethod
    def tearDown(cls):
        try:
            instance = Video.objects.first()
            path = pathlib.Path(instance.video.path)
        except:
            pass
        else:
            if path.exists():
                path.unlink()
                path.parent.rmdir()

    def test_video_categories(self):
        path = reverse('videos_api:categories')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)

        for item in response.json():
            with self.subTest(item=item):
                self.assertIn('title', item)

    def test_video_subcategories(self):
        path = reverse('videos_api:sub_categories', args=['sports'])
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('title', data[0])

    def test_list_videos(self):
        path = reverse('videos_api:videos')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('title', data[0])
        self.assertIn('user_channel', data[0])
        self.assertIn('user', data[0])

    def test_upload_video(self):
        path = reverse('videos_api:upload_video')

        small_video = SimpleUploadedFile(
            name='vid1.mp4',
            content=b'x',
            content_type='video/mp4'
        )

        form_data = {
            'video': small_video,
            'title': 'New video that I want to use',
            'description': 'Some simple description',
            'recording_location': 'Lille',
            'channel_playlist': ''
        }
        response = self.client.post(path, data=form_data, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_get_video(self):
        pass

    def test_viewing_profile(self):
        pass

    def test_list_user_videos(self):
        pass

    def test_feed_builder(self):
        path = reverse('videos_api:feed_builder_videos')
        response = self.client.post(path, data={
            'sources': [
                {

                }
            ]
        })
        print(response.content)


class TestCommentApiResponse(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    def setUp(self):
        super().setUp()
        self.video = Video.objects.first()

    def test_create_comment(self):
        response = self.client.post(
            reverse('videos_api:create_comment', args=[self.video.video_id]),
            data={
                'content': 'I am trying to write comment'
            }
        )
        print(response.content)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPAGATES=True)
class TestTasks(TransactionTestCase):
    fixtures = ['videos']

    def test_moderate_comment(self):
        video = Video.objects.first()
        t1 = tasks.get_video_frames


class TestViewingProfileView(APITestCase):
    def test_structure(self):
        path = reverse('viewing_profile_id')
        response = self.client.post(path)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())


class TestUtilities(IsolatedAsyncioTestCase):
    async def test_get_firebase(self):
        pass
        # client = get_firebase_app()
        # result = client.collection('vp_profiles')
        # await result.document('vp_123').set({'name': 'Google'})
        # print(result)
