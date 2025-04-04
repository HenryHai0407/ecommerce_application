from django.shortcuts import render, redirect
from products.models import Product
from .models import Order, OrderItem, Payment, Customer

# Create your views here.
def payment_view(request):
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('view_cart')

    if request.method == 'POST':
        # In a real scenario, here you would process payment details.
        # For simulation, we'll assume payment succeeds.
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Create or retrieve the customer
        customer, _ = Customer.objects.get_or_create(email=email, defaults={
            'name': name,
            'address': address,
            'phone': phone,
        })

        # Calcuate total price
        products = Product.objects.filter(id__id=cart.keys())
        total = sum(product.price * cart.get(str(product.id)) for product in products)

        # Create Order
        order = Order.objects.create(customer=customer, total_price = total)

        # Create Order Items
        for product in products:
            quantity = cart.get(str(product.id))
            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity,
                price = product.price
            )

        # Create payment record (simulation success)
        Payment.objects.create(
            order = order,
            payment_method = 'Simulated',
            transaction_id = 'EHAI123456',
            amount = total,
            success = True
        )

        # Clear the cart
        request.session['cart'] = {}

        # Redirect to a payment success page
        return redirect('payment_success')
    return render(request, 'products/payment.html')

def payment_success(request):
    return render(request, 'products/payment_success.html')