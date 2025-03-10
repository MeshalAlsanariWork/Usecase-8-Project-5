import streamlit as st
import requests

def get_prediction(type_encoding, price, area):
    url = 'https://bayut.onrender.com/predict/riyadh'
    data = {
        "Type_encoding": type_encoding,
        "Price": price,
        "Area_m2": area,
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get prediction"}

st.title("Property Price Prediction in Riyadh")

property_types = {
    0: "Apartment",
    7: "Villa",
    5: "Residential Land",
    1: "Building",
    3: "Land",
    2: "Floor",
    6: "Residential House",
    4: "Residential Building"
}

type_encoding = st.selectbox("Select Property Type", list(property_types.keys()), format_func=lambda x: property_types[x])
price = st.number_input("Enter Price", min_value=0, step=100)
area = st.number_input("Enter Area in m²", min_value=0, step=10)

if st.button("Get Prediction"):
    prediction = get_prediction(type_encoding, price, area)

    if "error" not in prediction:
        st.write(f"Predicted Price: {prediction.get('Price_Prediction')}")
    else:
        st.write(prediction["error"])