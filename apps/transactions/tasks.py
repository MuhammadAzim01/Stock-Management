from celery import shared_task
from decimal import Decimal
from django.db import transaction as db_transaction

from apps.transactions.models import Transaction
from apps.users.models import User
from apps.stocks.models import Stock

@shared_task
def test_task():
    print('test task')


@shared_task
def process_transaction(user_id, ticker, transaction_type, transaction_volume):
    try:
        with db_transaction.atomic():
            user = User.objects.select_for_update().get(id=user_id)
            current_stock = Stock.objects.get(ticker=ticker)
            
            transaction_price = current_stock.close_price
            total_amount = transaction_price * Decimal(transaction_volume)

            if transaction_type == Transaction.TransactionType.BUY:
                if user.balance < total_amount:
                    raise ValueError("Insufficient balance")
                user.balance -= total_amount
            else:
                user.balance += total_amount

            user.save()

            transaction = Transaction.objects.create(
                user=user,
                ticker=current_stock,
                transaction_type=transaction_type,
                transaction_volume=transaction_volume,
                transaction_price=transaction_price
            )

            return {
                "status": "success",
                "transaction_id": transaction.id
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }