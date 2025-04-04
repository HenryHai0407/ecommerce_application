# products/urls.py

from django.urls import path
from .views import home, products, add_to_cart, view_cart

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
]
