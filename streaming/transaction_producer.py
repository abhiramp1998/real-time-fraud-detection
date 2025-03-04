from kafka import KafkaProducer
import json
import time
import pandas as pd

# Load sample transactions
df = pd.read_csv("data/creditcard.csv").sample(500)  # Simulating a stream

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic_name = "fraud_transactions"

# Stream transactions in real-time
for _, row in df.iterrows():
    transaction = row.to_dict()
    producer.send(topic_name, value=transaction)
    print(f"📨 Sent: {transaction}")
    time.sleep(2)  # Simulating a delay

print("✅ Transaction streaming started!")
