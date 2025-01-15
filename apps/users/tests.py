from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', balance=1000.00)
        self.user_create_url = reverse('user-list')
        self.user_detail_url = reverse('user-detail', args=[self.user.username])

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'balance': 500.00
        }
        response = self.client.post(self.user_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_retrieve_user(self):
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
