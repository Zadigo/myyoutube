from django.contrib.auth import get_user_model
from comments.models import Comment
from django.urls import reverse
from rest_framework.test import APITestCase


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
                'username': self.user.username,
                'password': 'touparet'
            }
        )

        self.assertEqual(response.status_code, 200, response.content)

        token = response.json().get('access')
        self.assertIsNotNone(token, 'Token retrieval failed')

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        return token


class TestCommentApi(AuthenticationMixin):
    fixtures = ['fixtures/comments']

    def test_list_comments_unauthenticated(self):
        self.client.credentials()
        response = self.client.get(
            reverse('comments:list', args=['vid_12345']))
        self.assertEqual(response.status_code, 200)
        print(response.json())

    def test_create_comment(self):
        response = self.client.post(
            reverse('comments:create', args=['vid_12345']),
            data={
                'content': 'This is a test comment'
            }
        )
        self.assertEqual(response.status_code, 201, response.content)

    def test_create_reply(self):
        comment = Comment.objects.first()
        response = self.client.post(
            reverse('comments:reply', args=[comment.id]),
            data={
                'content': 'This is a test reply'
            }
        )
        self.assertEqual(response.status_code, 201, response.content)

    def test_retrieve_comments(self):
        response = self.client.get(
            reverse('comments:list', args=['vid_12345']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_update_comment(self):
        response = self.client.patch(
            reverse('comment-detail', args=[1]),
            data={
                'content': 'Updated comment content'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.get(
            id=1).content, 'Updated comment content')

    def test_delete_comment(self):
        response = self.client.delete(reverse('comment-detail', args=[1]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Comment.objects.count(), 2)
