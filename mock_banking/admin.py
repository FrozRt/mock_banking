from django.contrib import admin
from mock_banking.models import Account, Payment

# Register your models here.

admin.site.register(Account)
admin.site.register(Payment)
