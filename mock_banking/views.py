from .serializers import AccountSerializer, PaymentSerializer
from .models import Account, Payment
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .services import make_payment, check_account_exists
from .mixins import ServiceExceptionHandlerMixin


# Create your views here.

class AccountViewSet(generics.ListAPIView):
    """
    Concrete view for listing a queryset.
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class CreateOrGetPaymentView(ServiceExceptionHandlerMixin, generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    Because of ServiceExceptionHandlerMixin there is
    no need to handle exception manually.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        from_account = check_account_exists(self.request.data['from_account'])
        to_account = check_account_exists(self.request.data['to_account'])

        make_payment(
            from_account,
            to_account,
            float(self.request.data['amount']))

        return Response(serializer.data, status=status.HTTP_201_CREATED)
