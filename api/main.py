"""
main.py
FastAPI app for demand forecasting.
"""

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
from src.predict import predict_single, predict_batch

app = FastAPI(title="Retail Demand Forecasting API")

MODEL_PATH = "models/ridge_forecast_model.pkl"

class ForecastRequest(BaseModel):
    date: str
    item: str
    category: str
    brand: str
    price: float
    promotion: int
    discount: float

@app.post("/predict/")
def get_prediction(input_data: ForecastRequest):
    input_dict = input_data.dict()
    prediction = predict_single(input_dict, MODEL_PATH)
    return {"predicted_units_sold": round(prediction, 2)}

@app.post("/predict/batch/")
async def get_batch_prediction(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    preds = predict_batch(df, MODEL_PATH)
    df["predicted_units_sold"] = preds
    return df.to_dict(orient="records")
