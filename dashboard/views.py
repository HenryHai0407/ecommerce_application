# orders/views.py (or dashboard/views.py)
from django.shortcuts import render
from django.db.models import Sum
from products.models import Product
from orders.models import OrderItem

def dashboard(request):
    # Query OrderItem, grouping by product and summing the quantity sold
    best_selling = (
        OrderItem.objects
        .values('product__id','product__name')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')
    )
    context = {
        'best_selling': best_selling
    }
    return render(request,'products/dashboard.html', context)