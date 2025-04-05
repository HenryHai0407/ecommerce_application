# orders/urls.py

from django.urls import path
from .views import payment_view, payment_success

urlpatterns = [
    path('payment/', payment_view, name='payment'),
    path('payment-success/', payment_success, name='payment_success'),
]
