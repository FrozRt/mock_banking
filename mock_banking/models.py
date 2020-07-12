from django.db import models


# Create your models here.

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_username = models.CharField(max_length=128, null=False)
    email = models.EmailField()
    account_balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.account_username}'

    class Meta:
        db_table = "accounts"


class Payment(models.Model):
    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account'
    )
    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment from id={self.from_account_id} to id={self.to_account_id}' \
               f' for "{self.payment_date.strftime("%Y-%m-%d %H:%M:%S")}"'

    class Meta:
        db_table = "payments"
