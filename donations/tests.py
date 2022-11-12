from django.test import TestCase
from donations import views
from django.test.client import Client, RequestFactory

class TestDonation(TestCase):
    def test_send_donation(self):
        client = RequestFactory()
        request = client.post('donations/send', data={
            'channel_reference': None,
            'video_reference': None
            'value': None
        })
        result = views.send_donation(request)
        print(result)
