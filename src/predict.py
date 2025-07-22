"""
predict.py
Prediction wrapper functions for point and batch inference.
"""

import pandas as pd
from src.feature_engineer import add_time_features, encode_categoricals
from src.model import load_model

FORECAST_FEATURES = [
    'item', 'category', 'price', 'promotion', 'discount',
    'brand', 'day_of_week', 'month', 'is_weekend', 'is_holiday'
]

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    df = add_time_features(df)
    df = encode_categoricals(df)
    return df[FORECAST_FEATURES]

def predict_single(input_dict: dict, model_path: str):
    model = load_model(model_path)
    df = pd.DataFrame([input_dict])
    X = preprocess_input(df)
    return model.predict(X)[0]

def predict_batch(df: pd.DataFrame, model_path: str) -> pd.Series:
    model = load_model(model_path)
    X = preprocess_input(df)
    return model.predict(X)

# Example usage:
if __name__ == "__main__":
    input_data = {
        'item': 'Toothpaste',
        'category': 'Personal Care',
        'price': 2.99,
        'promotion': 1,
        'discount': 0.1,
        'brand': 'Colgate',
        'date': '2023-10-01'
    }
    model_path = 'models/ridge_forecast_model.pkl'  # Example model path
    print(predict_single(input_data, model_path))