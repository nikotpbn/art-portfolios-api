from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class UserLoginTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )

    def test_user_create_or_collect_token(self):
        """User check token created if in post save signal format"""
        token = Token.objects.get(user__email=self.admin_user.email)
        self.assertTrue(token.key)

    def test_user_authenticated(self):
        """Check if user is authenticated"""
        token = Token.objects.get(user__email=self.admin_user.email)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        r = self.client.get(reverse('user:me'))
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        """test user login"""
        url = reverse('user:login')
        data = {
                'username': 'admin@example.com',
                'password': 'testpass123'
            }
        r = self.client.post(url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(r.data['token'])