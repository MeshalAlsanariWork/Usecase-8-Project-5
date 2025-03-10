import streamlit as st
import requests

# Function to call the API
def get_prediction(type_encoding, price, area):
    url = 'https://bayut.onrender.com/predict/riyadh'
    data = {
        "Type_encoding": type_encoding,
        "Price": price,
        "Area_m2": area,
    }
    response = requests.post(url, json=data)
    
    # If the response is successful, return the JSON response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get prediction"}

# Streamlit UI
st.set_page_config(page_title="Riyadh Region Property Prediction", page_icon="🏠", layout="centered")

# Add some styling to the app
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput>div>div>input {
        background-color: #f0f8ff;
    }
    </style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="title">Riyadh Region</h1>', unsafe_allow_html=True)

# Mapping for property types
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

# Inputs for the user
type_encoding = st.selectbox(
    "Select Property Type",
    list(property_types.keys()), 
    format_func=lambda x: property_types[x],
    key="type"
)
price = st.number_input("Enter Price", min_value=0, step=100, key="price")
area = st.number_input("Enter Area in m²", min_value=0, step=10, key="area")

# Button to get prediction
if st.button("Get Prediction"):
    prediction = get_prediction(type_encoding, price, area)
    
    # Display the result
    if "error" not in prediction:
        st.markdown(f"<h3 style='text-align: center;'>Predicted Price: {prediction.get('Price_Prediction')} SAR</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='text-align: center; color: red;'>{prediction['error']}</h3>", unsafe_allow_html=True)