import streamlit as st
import joblib
import numpy as np

model = joblib.load("lead_scoring_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Lead Scoring Prediction System")

total_visits = st.number_input("Total Visits", 0, 100)

time_spent = st.number_input("Time Spent on Website", 0, 5000)

page_views = st.number_input("Page Views", 0.0, 50.0)

if st.button("Predict"):