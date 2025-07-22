"""
feature_engineer.py
Modular functions to add engineered features.
"""

import pandas as pd

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
    df['month'] = pd.to_datetime(df['date']).dt.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_holiday'] = 0  # Placeholder for future holiday integration
    return df

def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    item_map = {'Toothpaste': 0, 'Soap': 1, 'Diaper': 2}
    category_map = {'Personal Care': 0, 'Baby Care': 1}
    brand_map = {'Colgate': 0, 'Dove': 1, 'Pampers': 2}

    df['item'] = df['item'].map(item_map)
    df['category'] = df['category'].map(category_map)
    df['brand'] = df['brand'].map(brand_map)
    return df
