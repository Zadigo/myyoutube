from django.test import TestCase
from donations import views
from django.test.client import Client, RequestFactory

class TestDonation(TestCase):
    fixtures = ['donations']
    
    def test_send_donation(self):
        client = RequestFactory()
        request = client.post('donations/send', data={
            'channel_reference': 'google',
            'video_reference': 'google1',
            'value': 10
        })
        result = views.send_donation(request)
        print(result)
