import streamlit as st
import pickle
import pandas as pd

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Obesity Status Predictor")
st.write("Enter your details below.")

age = st.number_input("Age (years)", 1, 120, 23)
height = st.number_input("Height (metres)", 0.5, 2.5, 1.75)
weight = st.number_input("Weight (kg)", 1.0, 300.0, 70.0)

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[age, height, weight]],
        columns=["Age", "Height", "Weight"]
    )
    prediction = model.predict(input_data)
    st.success(f"Predicted obesity category: {prediction[0]}")
