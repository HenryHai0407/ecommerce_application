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

        # Get products from cart
        product_ids = [int(key) for key in cart.keys()]
        products = Product.objects.filter(id__in=product_ids)

        # Calculate total price
        total = sum(product.price * cart.get(str(product.id),0) for product in products)

        # Create Order
        order = Order.objects.create(customer=customer, total_price = total)

        # Create Order Items
        for product in products:
            quantity_purchased = cart.get(str(product.id))
            OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity_purchased,
                price = product.price
            )
            # Update product stock
            product.quantity = max(product.quantity - quantity_purchased, 0)
            product.save()

        # Generate unique transaction_id
        # Format: <order_id>-<customer_name>-<last_4_phone_digits>
        phone_digits = '0000' # Default if no phone number
        if customer.phone and len(customer.phone) >= 4:
            phone_digits = customer.phone[-4:] # Last 4 digits
        # Clean customer name (remove spaces, special characters for simplicity)
        clean_name = "noname"
        if customer.name:
            clean_name = ''.join(customer.name.split()[:2])[:10]
        transaction_id = f"{order.id}-{clean_name}-{phone_digits}"

        # Create payment record (simulation success)
        Payment.objects.create(
            order = order,
            payment_method = 'Simulated',
            transaction_id = transaction_id, 
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