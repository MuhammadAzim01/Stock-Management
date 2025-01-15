from django.urls import path

from apps.stocks.views import (
    StockListCreateView, 
    StockDetailView
)

urlpatterns = [
    path('stocks/', StockListCreateView.as_view(), name='stock-list'),
    path('stocks/<str:ticker>/', StockDetailView.as_view(), name='stock-detail'),
]
