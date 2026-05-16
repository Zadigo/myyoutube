from django.test import TransactionTestCase, override_settings
from notifications import tasks
from rest_framework.test import APITestCase


from django.contrib.auth import get_user_model
from django.test import TransactionTestCase, override_settings
from django.urls import reverse
from rest_framework.test import APITestCase
from notifications import tasks
from notificationsplatform.unittestmixins import AuthenticationMixin


class TestNotificationApi(AuthenticationMixin):
    fixtures = ['fixtures/notifications']

    def test_list_notifications(self):
        url = reverse('notifications:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response.json())

    def test_create_notification(self):
        url = reverse('notifications:create')
        data = {
            'user': self.user.id,
            'video': 'Test Video',
            'notification_type': 'Follow'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201, response.content)
