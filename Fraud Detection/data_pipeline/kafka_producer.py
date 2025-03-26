import random
import time
import json
from kafka import KafkaProducer

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Simulating transaction data
def generate_transaction():
    transaction = {
        "transaction_id": random.randint(1000, 9999),
        "amount": random.uniform(10, 500),
        "type": random.choice(['debit', 'credit']),
        "timestamp": time.time()
    }
    return json.dumps(transaction).encode('utf-8')

# Send simulated transactions to Kafka
def send_transactions():
    while True:
        transaction = generate_transaction()
        producer.send('transactions_topic', transaction)
        print(f"Sent transaction: {transaction}")
        time.sleep(1)  # Simulate real-time stream (1 transaction per second)

if __name__ == "__main__":
    send_transactions()