from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os


#load model
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_PATH = os.path.join(BASE_DIR, "../../", "models", "classifier.pkl")

# model = joblib.load(MODEL_PATH)

model = joblib.load("../../models/classifier.pkl")

#define expected input format
class MobileSpecs(BaseModel):
    battery_power: int
    blue: int
    clock_speed: float
    dual_sim: int
    fc: int
    four_g: int
    int_memory: int
    m_dep: float
    mobile_wt: int
    n_cores: int
    pc: int
    px_height: int
    px_width: int
    ram: int
    sc_h: int
    sc_w: int
    talk_time: int
    three_g: int
    touch_screen: int
    wifi: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mobile Price Prediction API is running."}

@app.post("/predict")
def predict_price(data: MobileSpecs):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"predicted_price_range": int(prediction)}