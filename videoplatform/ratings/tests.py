from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from videos.models import Video
from ratings.models import Rating


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


class TestRatingApi(AuthenticationMixin):
    fixtures = ['base_fixtures/videos']

    def setUp(self):
        super().setUp()
        self.video = Video.objects.first()

    def test_rate_video_when_not_exists(self):
        """Test for when there is not existing rating
        for the current video. Expected behaviour is that a
        new rating is created and returned"""
        path = reverse('ratings_api:rate_video', args=[self.video.video_id])
        data = {
            'liked': True,
            'unliked': False,
            'rating_for': 'Video',
            'subscription': {
                'active': False,
                'mode': None
            }
        }
        response = self.client.post(path, data=data, format='json')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIn('id', data)
        self.assertEqual(data['video']['id'], 1)
        self.assertEqual(data['rating_type'], 'Like')
        self.assertIn('video', data)

    def test_rate_video_when_exists(self):
        """Test for when there is not existing rating
        for the current video. Expected behaviour is that
        an attribute on the rating is modified"""
        Rating.objects.create(
            user=self.user,
            video=self.video,
            rating_for='Video'
        )

        path = reverse('ratings_api:rate_video', args=[self.video.video_id])
        data = {
            'liked': False,
            'unliked': True,
            'rating_for': 'Video',
            'subscription': {
                'active': False,
                'mode': None
            }
        }
        response = self.client.post(path, data=data, format='json')
        # self.assertEqual(response.status_code, 201)
        print(response.content)
