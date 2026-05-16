from comments.models import Comment
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from ratings.models import Rating
from commentsplatform.unittestmixins import AuthenticationMixin


class TestRatingApi(AuthenticationMixin):
    fixtures = ['fixtures/comments']

    def test_like_comment(self):
        data = {
            'liked': True,
            'unliked': False,
            'rating_for': 'Comment',
            'subscription': {
                'subscribed': True,
                'mode': 'All'
            }
        }

        comment = Comment.objects.first()

        response = self.client.post(
            reverse('ratings:rate', args=[comment.id]),
            data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201, response.content)
