#!/bin/bash

# Start API
uvicorn api.fraud_api:app --host 0.0.0.0 --port 8000 &

# Start Kafka producer
python streaming/transaction_producer.py &

# Start Fraud Detection Consumer
python streaming/fraud_detection.py &

# Start Dashboard
streamlit run dashboards/dashboard.py
