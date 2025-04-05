# products/urls.py

from django.urls import path
from .views import home, products, add_to_cart, view_cart, increase_quantity, decrease_quantity,clear_cart

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/increase/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/clear/',clear_cart, name='clear_cart'),

]
