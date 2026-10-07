
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("heart_failure_model.pkl")

st.title("Heart Failure Risk Prediction")
st.write("Enter the patient's clinical information below.")

age = st.number_input("Age", min_value=1, max_value=120, value=60)

anaemia = st.selectbox("Anaemia", ["No", "Yes"])
anaemia = 1 if anaemia == "Yes" else 0

creatinine_phosphokinase = st.number_input(
    "Creatinine Phosphokinase",
    min_value=0,
    value=250
)

diabetes = st.selectbox("Diabetes", ["No", "Yes"])
diabetes = 1 if diabetes == "Yes" else 0

ejection_fraction = st.number_input(
    "Ejection Fraction",
    min_value=0,
    max_value=100,
    value=38
)

high_blood_pressure = st.selectbox(
    "High Blood Pressure",
    ["No", "Yes"]
)
high_blood_pressure = 1 if high_blood_pressure == "Yes" else 0


platelets = st.number_input(
    "Platelets",
    min_value=0.0,
    value=250000.0
)

serum_creatinine = st.number_input(
    "Serum Creatinine",
    min_value=0.0,
    value=1.0
)

serum_sodium = st.number_input(
    "Serum Sodium",
    min_value=0.0,
    value=137.0
)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

smoking = st.selectbox("Smoking", ["No", "Yes"])
smoking = 1 if smoking == "Yes" else 0

if st.button("Predict Risk"):

    input_data = pd.DataFrame([[
        age,
        anaemia,
        creatinine_phosphokinase,
        diabetes,
        ejection_fraction,
        high_blood_pressure,
        platelets,
        serum_creatinine,
        serum_sodium,
        sex,
        smoking
    ]], columns=[
        'age',
        'anaemia',
        'creatinine_phosphokinase',
        'diabetes',
        'ejection_fraction',
        'high_blood_pressure',
        'platelets',
        'serum_creatinine',
        'serum_sodium',
        'sex',
        'smoking'
    ])

    probability = model.predict_proba(input_data)[0][1]

    if probability >= 0.25:
        st.error("Higher Risk of Death")
    else:
        st.success("Lower Risk of Death")

    st.write(f"Predicted probability: {probability:.2%}")
