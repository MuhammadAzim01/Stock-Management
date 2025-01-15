from rest_framework import generics
from rest_framework.response import Response

from apps.transactions.models import Transaction
from apps.transactions.serializers import TransactionSerializer
from apps.transactions.tasks import process_transaction


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        process_transaction.delay(
            user_id=request.data['user_id'],
            ticker=request.data['ticker'],
            transaction_type=request.data['transaction_type'],
            transaction_volume=request.data['transaction_volume']
        )
        # test_task.delay()
        return Response({"status": "Transaction processing started"})


class UserTransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user_id=user_id)


class UserTransactionTimeRangeView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        start_timestamp = self.kwargs['start_timestamp']
        end_timestamp = self.kwargs['end_timestamp']

        return Transaction.objects.filter(
            user_id=user_id,
            timestamp__range=[start_timestamp, end_timestamp]
        )
