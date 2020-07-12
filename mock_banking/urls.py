from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.CreateOrGetPaymentView.as_view()),
    path('accounts/', views.AccountViewSet.as_view()),
]
