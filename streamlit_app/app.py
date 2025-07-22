import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
import pandas as pd
from src.predict import predict_single, predict_batch

MODEL_PATH = "models/ridge_forecast_model.pkl"

st.title("🛒 Retail Demand Forecasting Dashboard")

tab1, tab2 = st.tabs(["📌 Point Forecast", "📂 Batch Forecast"])

with tab1:
    st.header("📌 Point Prediction")

    with st.form("point_form"):
        date = st.date_input("Forecast Date")
        item = st.selectbox("Item", ["Toothpaste", "Soap", "Diaper"])
        category = st.selectbox("Category", ["Personal Care", "Baby Care"])
        brand = st.selectbox("Brand", ["Colgate", "Dove", "Pampers"])
        price = st.number_input("Price", min_value=0.0, value=45.0)
        promotion = st.selectbox("Promotion", [0, 1])
        discount = st.slider("Discount", 0.0, 1.0, 0.0, 0.05)

        submitted = st.form_submit_button("Predict Demand")
        if submitted:
            input_dict = {
                "date": date.strftime("%Y-%m-%d"),
                "item": item,
                "category": category,
                "brand": brand,
                "price": price,
                "promotion": promotion,
                "discount": discount
            }
            prediction = predict_single(input_dict, MODEL_PATH)
            st.success(f"📦 Predicted Units Sold: **{prediction:.2f}**")

with tab2:
    st.header("📂 Batch Prediction")

    uploaded_file = st.file_uploader("Upload CSV with input data", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Data", df.head())
        preds = predict_batch(df, MODEL_PATH)
        df["predicted_units_sold"] = preds
        st.success("✅ Forecast complete")
        st.write("🔮 Predictions", df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Predictions", csv, "forecast_output.csv", "text/csv")
