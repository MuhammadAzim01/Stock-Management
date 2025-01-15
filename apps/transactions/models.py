from django.db import models

from apps.users.models import User
from apps.stocks.models import Stock


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        BUY = 'BUY', 'Buy'
        SELL = 'SELL', 'Sell'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    ticker = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(
        max_length=4,
        choices=TransactionType.choices
    )
    transaction_volume = models.IntegerField()
    transaction_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"{self.transaction_type} {self.transaction_volume} {self.ticker} by {self.user.username}"
