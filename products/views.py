from django.shortcuts import render
from django.db.models import Q
from .models import Product

# Create your views here.
# Home page view
def home(request):
    return render(request,'products/home.html')

def products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(request,'products/products.html',{'products': products,'query':query})
