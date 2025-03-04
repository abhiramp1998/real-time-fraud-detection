from fastapi import FastAPI
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Real-Time Fraud Detection API is running!"}

@app.post("/predict")
def predict_fraud(transaction: dict):
    # Extract transaction details
    data = pd.DataFrame([transaction])
    
    # Select relevant features (ensure same preprocessing as training)
    data['TransactionHour'] = pd.to_datetime(data['Time'], unit='s').dt.hour
    data['AmountLog'] = np.log1p(data['Amount'])
    X = data[['TransactionHour', 'AmountLog']]

    # Predict fraud
    prediction = model.predict(X)[0]  # -1 for fraud, 1 for normal
    fraud_label = 1 if prediction == -1 else 0
    
    return {"fraud_prediction": fraud_label}

# To run: `uvicorn api.fraud_api:app --reload`
