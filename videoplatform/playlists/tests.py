
from videos.models import Video
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from playlists.models import Playlist


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

        self.assertEqual(response.status_code, 200, msg=response.content)

        token = response.json().get('access')
        self.assertIsNotNone(token, 'Token retrieval failed')

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        return token


class TestPlaylistApi(AuthenticationMixin):
    fixtures = ['base_fixtures/videos', 'playlists']

    def test_list_items(self):
        path = reverse('playlists_api:list')
        response = self.client.get(path)
        data = response.json()
        self.assertEqual(response.status_code, 200, msg=response.content)

    def test_create(self):
        path = reverse('playlists_api:create')
        data = {
            'name': 'Music from Taylors',
            'description': 'Some music items from Taylors',
            'visibility': 'Public',
            'is_intelligent': False
        }
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, 201, msg=response.content)

    def test_add_video(self):
        playlist = Playlist.objects.first()
        video = Video.objects.first()
        path = reverse('playlists_api:add_video', args=[playlist.playlist_id])
        data = {'video_id': video.video_id}
        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, 200, msg=response.content)

        data = response.json()
        self.assertEqual(data[0]['name'], 'Test playlist')

        for item in data[0]['videos']:
            with self.subTest(item=item):
                self.assertEqual(item['title'], 'Simple video name')
