from kafka import KafkaConsumer
import json
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("models/model.pkl")

# Kafka Consumer
consumer = KafkaConsumer(
    "fraud_transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("✅ Listening for transactions...")

for message in consumer:
    transaction = message.value
    data = pd.DataFrame([transaction])
    
    # Extract relevant features
    data['TransactionHour'] = pd.to_datetime(data['Time'], unit='s').dt.hour
    data['AmountLog'] = np.log1p(data['Amount'])
    X = data[['TransactionHour', 'AmountLog']]

    # Predict fraud
    prediction = model.predict(X)[0]
    fraud_label = 1 if prediction == -1 else 0

    if fraud_label == 1:
        print(f"⚠️ FRAUD DETECTED: {transaction}")

print("✅ Fraud detection running...")
