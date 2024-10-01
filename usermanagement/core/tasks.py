import redis
import json
from django_rq import job
from .models import Product, Payment
from django.utils import timezone

# Redis connection
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Define a background task to listen for payment events from Redis
@job
def listen_for_payment_events():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('payment_events')  # Subscribe to the 'payment_events' channel

    for message in pubsub.listen():
        if message['type'] == 'message':
            try:
                payment_data = json.loads(message['data'].decode('utf-8'))
                process_payment_event(payment_data)
            except Exception as e:
                print(f"Error processing payment event: {str(e)}")

# Function to process payment event
def process_payment_event(payment_data):
    user_id = payment_data.get('user_id')
    product_id = payment_data.get('product_id')
    amount = payment_data.get('amount')
    transaction_id = payment_data.get('transaction_id', '')
    timestamp = payment_data.get('transaction_time', timezone.now().isoformat())

    # Find the product
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} does not exist.")
        return

    # Simulate saving the payment to the database
    Payment.objects.create(
        user_id=user_id,
        product=product,
        amount=amount,
        transaction_id=transaction_id,
        timestamp=timestamp
    )

    print(f"Payment event processed: {user_id} bought {product.name} for ${amount}.")

