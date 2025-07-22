# 🛒 Retail Demand Forecasting

This project builds a machine learning pipeline to forecast future product demand in a retail setting. It uses historical sales, promotions, prices, and time-based signals to accurately predict units sold for various retail items such as toothpaste, soap, and diapers.

---

## 📁 Project Structure

```
retail-demand-forecasting/
│
├── config/                      # Configuration files (e.g., model parameters)
│   └── params.yaml
│
├── data/
│   ├── raw/                     # Original raw data (if any)
│   └── processed/               # Cleaned and feature-engineered datasets
│       └── retail_sales_extended.csv
│       └── retail_sales_features.csv
│
├── notebooks/                  # Jupyter notebooks for exploration and modeling
│   ├── 01_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_forecasting.ipynb
│
├── models/                     # Trained model artifacts
│
├── src/                        # Python source files
│   ├── data_loader.py
│   ├── feature_engineer.py
│   ├── model.py
│   └── predict.py
│
├── requirements.txt            # Python package dependencies
└── README.md                   # Project overview and setup instructions
```

---

## 🚀 Key Features

- Forecasts daily demand using:
  - Product-level features: item, category, brand, price, discount
  - Time-based features: day of week, month, is holiday
  - Promotion and inventory signals
  - Lag and rolling average sales trends
- Supports scalable training with a single global model
- Clean modular design with Jupyter + Python scripts

### ⚠️ Forecasting-Time Feature Limitations

At forecasting time (i.e., when predicting for future dates), some features used during model training are **not available** and were therefore **excluded from the final Ridge regression model**:

#### ❌ Excluded Features:
1. **Lag and Rolling Average Sales Features**
   - `sales_lag_1`, `sales_lag_3`, `sales_lag_7`
   - `sales_7d_avg`, `sales_30d_avg`, `sales_30d_trend`
   - These depend on **future sales** that haven't happened yet.

2. **Inventory Signals**
   - `stock_available`, `stockout_flag`
   - These are only known in real-time, not ahead of time.

#### ✅ Solution:
We retrained the final Ridge model using only the **"forecast-safe" features**:
- `item`, `category`, `price`, `promotion`, `discount`
- `brand`, `day_of_week`, `month`, `is_weekend`, `is_holiday`

This ensures the model can make reliable forecasts using only known or planned inputs.

---

## 📦 Setup

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run notebooks in order:
   - `01_exploration.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_training.ipynb`
   - `04_forecasting.ipynb`

---

## 🧠 Models Supported

- XGBoost (default)
- LightGBM (optional)
- Scikit-learn regressors

---

## 📊 Dataset

- The dataset is a synthetic but realistic simulation with ~2,000 rows
- Stored in: `data/processed/retail_sales_extended.csv`

Includes:
- `units_sold` (target)
- `item`, `category`, `brand`
- `price`, `promotion`, `discount`
- `stock_available`, `stockout_flag`
- Time features like `date`, `day_of_week`, `is_holiday`
- Engineered lags and trends

---

## 📈 Output

The final model predicts:
```
units_sold for each item on a given future date
```

This helps retail teams:
- Prevent stockouts
- Optimize inventory levels
- Plan promotions more effectively

---

📄 **[Extended Project Documentation →](docs/EXTENDED_PROJECT_DOCUMENTATION.md)**
Covers full project lifecycle, deployment, testing, and enhancement roadmap.

---

## 🙋‍♂️ Author

> Built by **[Sumit Das](https://www.linkedin.com/in/sumit-das-ai/)** – AI Engineer | GenAI | MLOps

