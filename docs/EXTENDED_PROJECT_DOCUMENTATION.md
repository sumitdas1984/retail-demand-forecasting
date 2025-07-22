# 📚 Extended Project Documentation

This document complements the main `README.md` with a detailed overview of the entire lifecycle of the Retail Demand Forecasting project — from problem framing to deployment and testing.

---

## ✅ Project Summary

**Goal:** Predict daily demand for retail products such as toothpaste, soap, and diapers.  
**Scope:** Build an end-to-end ML pipeline — data → features → model → API → dashboard.

---

## 🧱 Project Components

| Component | Status |
|-----------|--------|
| Data generation & processing | ✅ Done |
| Feature engineering | ✅ Done |
| Model training & evaluation | ✅ Ridge (best) |
| Forecasting future demand | ✅ Done |
| API deployment (FastAPI) | ✅ Live on Render |
| Streamlit dashboard (local) | ✅ Operational |
| Unit testing | ✅ `pytest` tested |
| Docker support | ✅ Dockerfile ready |

---

## 🔍 Problem Understanding

We forecast **`units_sold` per product per date** to:
- Avoid stockouts
- Optimize inventory
- Inform promotion planning

---

## 🧾 Feature Engineering

### Engineered features:
- `day_of_week`, `month`, `is_weekend`, `is_holiday`
- `item`, `brand`, `category`, `promotion`, `discount`
- (Training only) `sales_lag_1`, `sales_7d_avg`, `sales_30d_trend`
- (Training only) `stock_available`, `stockout_flag`

---

## 🧠 Model Training

We evaluated:
- ✅ **Ridge Regression** – best performance
- ❌ XGBoost, Random Forest – overfitting
- ✅ Linear, Lasso – also solid baselines

Metrics used: `MAE`, `RMSE`

---

## 📈 Forecasting Approach

- Final model excludes features not available at forecast time:
  - ❌ Lag features (future unknown)
  - ❌ Inventory signals
- Forecasts are generated using:
  - Known values like price, promotion, date, etc.

---

## 🌐 API Deployment (FastAPI)

Deployed to **Render** with two endpoints:
- `POST /predict` – point prediction
- `POST /predict/batch` – batch forecast via CSV

Uses `uvicorn` with proper PYTHONPATH and Ridge model.

---

## 🧪 Testing

- ✅ Unit tests for `predict_single()` and `predict_batch()` in `tests/test_predict.py`
- ✅ Verified model predictions
- ✅ Tested via `curl`, `pytest`, and Swagger UI

---

## 🖥️ Streamlit Dashboard

- **Local dashboard UI** with:
  - 📌 Point forecast form
  - 📂 Batch CSV upload & download
- Will be decoupled from model and connected to live API in future

---

## 🐳 Docker Support

- `Dockerfile` included for containerized deployments
- Streamlined setup with `pip install -r requirements.txt` and `uvicorn` as entrypoint

---

## 🚀 What’s Next?

| Opportunity | Description |
|-------------|-------------|
| 🧠 Hyperparameter tuning | Improve Ridge/Tree performance |
| 🌐 Deploy Streamlit | As a Render or EC2 app |
| 🔐 Add authentication | API key or OAuth security |
| 📊 Dashboard enhancement | Add charts, filters, trend graphs |
| 🧪 CI pipeline | Add GitHub Actions for tests |

---

Built and maintained by **[Sumit Das](https://www.linkedin.com/in/sumit-das-ai/)** – AI Engineer | GenAI | MLOps
