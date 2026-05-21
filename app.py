
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_pipeline.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure Months",
    0,
    100,
    12
)

monthly = st.number_input(
    "Monthly Charges",
    0.0,
    500.0,
    70.0
)

total = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

input_df = pd.DataFrame({
    "Gender": [gender],
    "Senior Citizen": [senior],
    "Tenure Months": [tenure],
    "Monthly Charges": [monthly],
    "Total Charges": [total],
    "Contract": [contract],
    "Internet Service": [internet],
    "Payment Method": [payment]
})

if st.button("Predict"):

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer not likely to churn")
