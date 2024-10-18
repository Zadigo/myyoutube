from accounts.views import LoginView, SignupView
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import Client, RequestFactory, TestCase

USER_MODEL = get_user_model()

class LoginTest(TestCase):
    fixtures = ['accounts']

    def setUp(self):
        self.factory = RequestFactory()

    def test_login_view(self):
        request = self.factory.get(reverse('accounts:login'))
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        client = Client()
        data = {'email': 'google@gmail.com', 'password': 'touparet'}
        response = client.post(reverse('accounts:login'), data)
        self.assertEqual(response.status_code, 200)
