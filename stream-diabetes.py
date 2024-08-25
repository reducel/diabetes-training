import pickle

import streamlit as st

# read model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# title
st.title("Data Mining For Predict Diabetes")

Pregnancies = st.text_input("Input Pregnancies")

Glucose = st.text_input("Input Glucose")

BloodPressure = st.text_input("Input Blood Pressure")

SkinThickness = st.text_input("Input Skin Thickness")

Insulin = st.text_input("Input Insulin")

BMI = st.text_input("Input BMI")

DiabetesPedigreeFunction = st.text_input("Input Diabetes Pedigree Function")

Age = st.text_input("Input Age")

# Code Predict
diabetes_diagnosa = ""

# Button for Predict
if st.button("Predict Patient"):
    diabetes_predict = diabetes_model.predict(
        [
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]
        ]
    )
    if diabetes_predict[0] == 1:
        diabetes_diagnosa = "Patients with Diabetes"
    else:
        diabetes_diagnosa = "Patients with No Diabetes"
    st.success(diabetes_diagnosa)
