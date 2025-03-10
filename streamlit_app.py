import streamlit as st
import requests

# Property type mapping
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

# Price category mapping
price_categories = {
    "Riyadh": {0: "Avg Price", 1: "Low Price", 2: "High Price"},
    "Eastern": {0: "Avg Price", 1: "Low Price", 2: "High Price"},
    "Western": {0: "Avg Price", 1: "High Price", 2: "Low Price"},
    "Southern": {0: "Low Price", 1: "Avg Price", 2: "High Price"}
}

def get_prediction(type_encoding, price, area_m2, region):
    url = f'https://bayut.onrender.com/predict/{region.lower()}'
    data = {
        "Type_encoding": type_encoding,
        "Price": price,
        "Area_m2": area_m2,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

# Streamlit UI
st.set_page_config(page_title="Real Estate Cluster", layout="centered")

# Apply custom background color
page_bg = """
<style>
    .stApp {
        background-color: #D2B48C;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🏡 Real Estate Price Cluster")
st.write("Fill in the details below to get a price Cluster.")

# User inputs
region = st.selectbox("🌍 Select Region", ["Riyadh", "Eastern", "Western", "Southern"])
col1, col2 = st.columns(2)
with col1:
    type_encoding = st.selectbox("🏠 Select Property Type", options=list(property_types.keys()), format_func=lambda x: property_types[x])
with col2:
    price = st.number_input("💰 Enter Price", min_value=0.0, step=1000.0)
area_m2 = st.slider("📏 Select Area (m²)", min_value=10, max_value=1000, step=10)

# Prediction Button
if st.button("🔮 Predict Price Cluster"):
    with st.spinner("Fetching prediction..."):
        result = get_prediction(type_encoding, price, area_m2, region)
    
    if "error" in result:
        st.error(f"❌ Error {result['error']}: {result['message']}")
    else:
        st.success("✅ Prediction Successful!")
        if "prediction" in result and isinstance(result["prediction"], list):
            prediction_value = result["prediction"][0]  # Extract the first value from the list
            price_category = price_categories.get(region, {}).get(prediction_value, "Unknown")
            st.write(f"🔢 **Predicted Price Category:** {price_category}")
        else:
            st.json(result)
            
