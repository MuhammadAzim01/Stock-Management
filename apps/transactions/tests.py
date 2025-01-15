from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from datetime import timedelta

from apps.users.models import User
from apps.stocks.models import Stock
from apps.transactions.models import Transaction


class TransactionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', balance=1000.00)
        self.stock = Stock.objects.create(
            ticker='AAPL',
            open_price=150.00,
            close_price=155.00,
            high=157.00,
            low=149.00,
            volume=1000000
        )
        self.transaction_url = reverse('transaction-create')
        self.user_transactions_url = reverse('user-transactions', args=[self.user.id])
        self.user_transactions_timerange_url = reverse(
            'user-transactions-timerange',
            args=[self.user.id, '2025-1-10T00:00:00Z', '2025-1-16T23:59:59Z']
        )

    def test_create_transaction(self):
        data = {
            'user_id': self.user.id,
            'ticker': self.stock.ticker,
            'transaction_type': Transaction.TransactionType.BUY,
            'transaction_volume': 10
        }
        response = self.client.post(self.transaction_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Transaction processing started')

    def test_list_user_transactions(self):
        Transaction.objects.create(
            user=self.user,
            ticker=self.stock,
            transaction_type=Transaction.TransactionType.BUY,
            transaction_volume=10,
            transaction_price=155.00
        )
        response = self.client.get(self.user_transactions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_list_user_transactions_within_timerange(self):
        transaction_time = timezone.now() - timedelta(days=5)
        Transaction.objects.create(
            user=self.user,
            ticker=self.stock,
            transaction_type=Transaction.TransactionType.BUY,
            transaction_volume=10,
            transaction_price=155.00
        )
        response = self.client.get(self.user_transactions_timerange_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
