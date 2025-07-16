from fastapi import APIRouter, HTTPException
import pandas as pd
from loguru import logger
import requests

from schemas import PredictionRequest
from config import DATA_API_URL

router = APIRouter()


@router.get("/")
async def home():
    return {"message": "The server is up and running!"}


@router.get("/health")
async def heath():
    return {"status": "ok"}


@router.post("/predict")
async def predict(prediction_request: PredictionRequest):
    try:
        response = requests.post(
            f"{DATA_API_URL}/users", json=prediction_request.dict()
        )
        if response.status_code == 200:
            logger.info(f"Profile successfully registered: {response.text}")
        else:
            logger.error(f"Error during profile registration: {response.text}")
    except Exception as err:
        detail_message = f"Connection error to the Data API: {err}"
        logger.error(detail_message)
        raise HTTPException(status_code=500, detail=detail_message)
    # try:
    #     df = pd.DataFrame([prediction_request.model_dump()])
    #     manually_processed_client = apply_manual_transformations(df)
    #     processed_client = preprocessor.transform(manually_processed_client)
    #     prediction_array = model_predict(model, processed_client)
    #     prediction_value = round(prediction_array[0], 2)
    #     logger.info(
    #         f"prediction: {prediction_value} avec le client suivant : {prediction_request}"
    #     )
    #     return {"prediction": str(prediction_value)}
    # except Exception as e:
    #     logger.error(
    #         f"Prediction processing error for profile {prediction_request.model_dump()}: {e}"
    #     )
    #     detail_message = f"Something went wrong during prediction: {e}"
    #     raise HTTPException(status_code=500, detail=detail_message)
