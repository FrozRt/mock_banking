from .models import Account, Payment
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_id', 'account_username', 'email', 'account_balance', 'created_at',
                  'last_activity_at')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'from_account', 'to_account', 'amount')
