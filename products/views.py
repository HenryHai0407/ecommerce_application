from django.shortcuts import render, redirect, get_object_or_404
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

def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart',{})

    # Increase quantity if product already in cart
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart',{})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart.get(str(product.id),0)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append(
            {
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            }
        )
    return render(request, 'products/cart.html', {"cart_items": cart_items, "total": total})
