from .models import Account, Payment
from django.db import transaction


def make_payment(from_account, to_account, amount):
    if from_account.account_balance < amount:
        raise (ValueError('Not enough money'))
    if from_account == to_account:
        raise (ValueError('Choose another account'))

    with transaction.atomic():
        from_balance = from_account.account_balance - amount
        from_account.account_balance = from_balance
        from_account.save()

        to_balance = to_account.account_balance + amount
        to_account.account_balance = to_balance
        to_account.save()

        payment = Payment.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount
        )

    return payment


def check_account_exists(account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Exception as e:
        print(e)
        raise ValueError('No such account')

    return account
