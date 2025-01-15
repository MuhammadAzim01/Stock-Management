from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.stocks.models import Stock


class StockAPITestCase(APITestCase):
    def setUp(self):
        self.stock = Stock.objects.create(
            ticker='AAPL',
            open_price=150.00,
            close_price=155.00,
            high=157.00,
            low=149.00,
            volume=1000000
        )
        self.stock_list_url = reverse('stock-list')
        self.stock_detail_url = reverse('stock-detail', args=[self.stock.ticker])

    def test_create_stock(self):
        data = {
            'ticker': 'GOOGL',
            'open_price': 2800.00,
            'close_price': 2850.00,
            'high': 2900.00,
            'low': 2750.00,
            'volume': 1500000
        }
        response = self.client.post(self.stock_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stock.objects.count(), 2)

    def test_retrieve_stock(self):
        response = self.client.get(self.stock_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ticker'], self.stock.ticker)
