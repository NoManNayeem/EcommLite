from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import Product, Payment
import redis
import json
from django.utils import timezone
import uuid

# Redis connection setup
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Display the list of products, accessible without login
def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'core/product_list.html', {'products': products})

# Display product details, accessible without login
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Fetch the product by its primary key (id)
    return render(request, 'core/product_detail.html', {'product': product})

# Process the payment for the selected product, login required
@login_required
def process_payment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # User and payment details
    user = request.user
    transaction_id = str(uuid.uuid4())
    amount = product.price
    timestamp = timezone.now()

    # Save the payment to the database
    Payment.objects.create(
        user=user,
        product=product,
        amount=amount,
        transaction_id=transaction_id,
        timestamp=timestamp
    )

    # Pass product details to the payment success page
    return render(request, 'core/payment_success.html', {
        'product': product,
        'transaction_id': transaction_id,
        'amount': amount,
        'timestamp': timestamp,
    })

# Display payment success page after payment is done
@login_required
def payment_success(request):
    return render(request, 'core/payment_success.html')

# Custom logout view that redirects to the product list after logout
def logout(request):
    auth_logout(request)  # Use Django's built-in logout function
    return redirect('product_list')  # Redirect to the product list after logout

# Display payment history for logged-in users
@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-timestamp')  # Get payments for the logged-in user
    return render(request, 'core/payment_history.html', {'payments': payments})
