from django.urls import path
from apps.transactions.views import (
    TransactionCreateView, 
    UserTransactionListView,
    UserTransactionTimeRangeView
)


urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/<int:user_id>/', UserTransactionListView.as_view(), name='user-transactions'),
    path(
        'transactions/<int:user_id>/<str:start_timestamp>/<str:end_timestamp>/',
        UserTransactionTimeRangeView.as_view(),
        name='user-transactions-timerange'
    ),
]
