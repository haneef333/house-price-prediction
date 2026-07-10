import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("notebooks/house_price_xgboost.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📌 Project Information")

st.sidebar.write("### 🤖 Model")
st.sidebar.success("XGBoost Regressor")

st.sidebar.write("### 📊 Dataset")
st.sidebar.info("California Housing Dataset")

st.sidebar.write("### 👨‍💻 Developer")
st.sidebar.write("Mohammed Haneef")

st.sidebar.markdown("---")
st.sidebar.write(
    "This application predicts California house prices using a trained "
    "XGBoost Machine Learning model."
)

# -----------------------------
# Main Title
# -----------------------------
st.title("🏠 California House Price Prediction")

st.markdown("""
Predict California house prices using a trained **XGBoost Machine Learning Model**.

Enter the house details below and click **Predict House Price**.
""")

st.divider()

# -----------------------------
# Input Section
# -----------------------------
st.subheader("🏡 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    medinc = st.number_input(
        "Median Income",
        min_value=0.0,
        value=3.5
    )

    averooms = st.number_input(
        "Average Rooms",
        min_value=1.0,
        value=5.0
    )

    population = st.number_input(
        "Population",
        min_value=1.0,
        value=1000.0
    )

    latitude = st.number_input(
        "Latitude",
        value=34.0
    )

with col2:
    houseage = st.number_input(
        "House Age",
        min_value=1.0,
        value=25.0
    )

    avebedrms = st.number_input(
        "Average Bedrooms",
        min_value=0.5,
        value=1.0
    )

    aveoccup = st.number_input(
        "Average Occupancy",
        min_value=1.0,
        value=3.0
    )

    longitude = st.number_input(
        "Longitude",
        value=-118.0
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict House Price"):

    input_data = pd.DataFrame({
        "MedInc": [medinc],
        "HouseAge": [houseage],
        "AveRooms": [averooms],
        "AveBedrms": [avebedrms],
        "Population": [population],
        "AveOccup": [aveoccup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    prediction = model.predict(input_data)

    predicted_price = prediction[0] * 100000

    st.success("✅ Prediction Completed!")

    st.metric(
        label="🏠 Estimated House Price",
        value=f"${predicted_price:,.2f}"
    )

    st.balloons()