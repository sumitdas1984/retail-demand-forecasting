"""
data_loader.py
Utility functions to load raw or processed data.
"""

import pandas as pd

def load_processed_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)
