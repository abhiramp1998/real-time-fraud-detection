import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib  # For saving the model

# Load dataset (Use a public dataset or your own)
df = pd.read_csv("data/creditcard.csv")  # Update this with your dataset

# Feature Engineering (Example)
df['TransactionHour'] = pd.to_datetime(df['Time'], unit='s').dt.hour
df['AmountLog'] = np.log1p(df['Amount'])

# Select features
features = ['TransactionHour', 'AmountLog']
X = df[features]

# Train Isolation Forest Model
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(X)

# Save model
joblib.dump(model, "models/model.pkl")

print("✅ Model training complete. Saved as models/model.pkl")
