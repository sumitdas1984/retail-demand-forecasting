"""
Unit tests for src/predict.py
"""

import pytest
import pandas as pd
from src.predict import predict_single, predict_batch

MODEL_PATH = "models/ridge_forecast_model.pkl"

def test_predict_single_valid():
    input_data = {
        "date": "2025-08-10",
        "item": "Toothpaste",
        "category": "Personal Care",
        "brand": "Colgate",
        "price": 45.0,
        "promotion": 0,
        "discount": 0.0
    }
    prediction = predict_single(input_data, MODEL_PATH)
    assert isinstance(prediction, float)

def test_predict_batch_valid():
    batch_df = pd.DataFrame([
        {
            "date": "2025-08-10",
            "item": "Toothpaste",
            "category": "Personal Care",
            "brand": "Colgate",
            "price": 45.0,
            "promotion": 0,
            "discount": 0.0
        },
        {
            "date": "2025-08-11",
            "item": "Soap",
            "category": "Personal Care",
            "brand": "Dove",
            "price": 25.0,
            "promotion": 0,
            "discount": 0.1
        }
    ])
    predictions = predict_batch(batch_df, MODEL_PATH)
    assert len(predictions) == 2
    assert all(isinstance(p, float) for p in predictions)
