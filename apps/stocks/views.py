from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.core.cache import cache

from apps.stocks.models import Stock
from apps.stocks.serializers import StockSerializer


class StockListCreateView(generics.ListCreateAPIView):
    serializer_class = StockSerializer
    
    def get_queryset(self):
        cache_key = 'all_stocks'
        queryset = cache.get(cache_key)
        
        if not queryset:
            queryset = Stock.objects.all().order_by('-updated_at')
            cache.set(cache_key, queryset, timeout=300)
        
        return queryset


class StockDetailView(generics.RetrieveAPIView):
    serializer_class = StockSerializer
    lookup_field = 'ticker'
    lookup_url_kwarg = 'ticker'
    
    def get_object(self):
        ticker = self.kwargs.get('ticker')
        cache_key = f'stock_{ticker}'
        stock = cache.get(cache_key)
        
        if not stock:
            try:
                stock = Stock.objects.get(ticker=ticker)
                cache.set(cache_key, stock, timeout=300)
            except Stock.DoesNotExist:
                raise NotFound("Stock not found")
        
        return stock
