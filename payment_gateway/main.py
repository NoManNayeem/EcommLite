from fastapi import FastAPI
import redis
import json
from pydantic import BaseModel
from cryptography.fernet import Fernet
import threading
from datetime import datetime

app = FastAPI()

# Redis connection setup
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Encryption setup for payment data (simulated)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Payment model for incoming payment requests
class PaymentRequest(BaseModel):
    user_id: int
    product_id: int
    amount: float
    transaction_id: str
    transaction_time: str

# Function to simulate payment processing and publish results back to Redis
def process_payment(payment_data):
    try:
        # Simulate payment processing (Encrypt the amount)
        encrypted_amount = cipher_suite.encrypt(str(payment_data['amount']).encode())
        print(f"Processing payment for User {payment_data['user_id']} for Product {payment_data['product_id']}.")

        # Simulate successful payment and publish result back to Redis
        payment_result = {
            'user_id': payment_data['user_id'],
            'product_id': payment_data['product_id'],
            'amount': payment_data['amount'],
            'transaction_id': payment_data['transaction_id'],
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }

        redis_client.publish('payment_results', json.dumps(payment_result))
        print(f"Payment processed successfully for User {payment_data['user_id']}.")
    except Exception as e:
        print(f"Error processing payment: {e}")

# Background thread to listen for payment events from Redis
def listen_for_payment_events():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('payment_events')  # Listen to the 'payment_events' channel

    for message in pubsub.listen():
        if message['type'] == 'message':
            try:
                payment_data = json.loads(message['data'].decode('utf-8'))
                process_payment(payment_data)
            except Exception as e:
                print(f"Error reading payment event: {str(e)}")

# Start a background thread to listen for payment events when FastAPI starts
thread = threading.Thread(target=listen_for_payment_events)
thread.start()

@app.get("/")
def read_root():
    return {"message": "FastAPI payment gateway is running and listening for payment events."}
