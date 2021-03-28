from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from fbprophet import Prophet
from fbprophet.serialize import model_to_json, model_from_json
import numpy as np
import json

app = FastAPI()

class Data(BaseModel):
    numHours: int = 24

@app.post("/prophecise/")
async def create_item(data: Data):
    #full_data = pd.read_pickle('D:\\DataScience\\HooHacks\\fbprophet\\solardata.pkl')

    with open('/app/serialized_model.json', 'r') as fin:
        model = model_from_json(json.load(fin))  # Load model

    future = model.make_future_dataframe(periods=data.numHours, freq='H') 

    future['cap'] = 120
    future.cap = np.cbrt(future.cap)

    forecast = model.predict(future)
    forecast.yhat = forecast.yhat**3
    # forecast = forecast[['ds', 'yhat']]

    print(list(forecast[['ds']].values))

    return [forecast[['ds']], forecast[['yhat']]]



@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python 3.6 or something"
    return {"message": message}