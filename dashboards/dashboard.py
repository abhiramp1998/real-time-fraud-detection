import streamlit as st
import pandas as pd
import os


st.title("🚀 Real-Time Fraud Detection Dashboard")

# Display detected fraud transactions
if "fraud_transactions.csv" in os.listdir("data"):
    df = pd.read_csv("data/fraud_transactions.csv")
    st.write(df)
else:
    st.write("No fraud transactions detected yet.")
