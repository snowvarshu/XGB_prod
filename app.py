from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

model_package = r"C:/Users/jenifer/Downloads/XGBoost_Model/crop_pattern_model_XGB.joblib"

package = joblib.load(
    "crop_pattern_model_XGB.joblib"
)


package = joblib.load(model_package)
mean_model = package["mean_model"]
median_model = package["median_model"]

valid_values = package["valid_values"]

app = FastAPI(title="Crop Pattern API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def validate_input(
    crop,
    season,
    state
):
    crop = crop.lower().strip()
    season = season.lower().strip()
    state = state.lower().strip()

    if crop not in valid_values["crops"]:
        raise ValueError("Invalid crop")

    if season not in valid_values["seasons"]:
        raise ValueError("Invalid season")

    if state not in valid_values["states"]:
        raise ValueError("Invalid state")

    return crop, season, state

class CropRequest(BaseModel):
    crop: str
    crop_year: int
    season: str
    state: str
    area: float
    yield_val: float = Field(..., alias="yield")
    method: str  
    
@app.post("/predict")
def predict(data: CropRequest):
    try:
        crop, season, state = validate_input(
            data.crop,
            data.season,
            data.state
        )

        method = data.method.lower().strip()

        if method == "mean":
            model = mean_model
        elif method == "median":
            model = median_model
        else:
            return {
                "error": "Method must be mean or median"
            }

        new_data = pd.DataFrame([{
            "crop": crop,
            "crop_year": data.crop_year,
            "season": season,
            "state": state,
            "area": data.area,
            "yield": data.yield_val
        }])

        score = float(model.predict(new_data)[0])

        status = (
            "Great cropping pattern"
            if score >= 70 else
            "Good cropping pattern"
            if score >= 60 else
            "Average cropping pattern"
            if score >= 40 else
            "Bad cropping pattern"
        )

        return {
            "cropping_pattern_score": round(score, 2),
            "status": status,
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Crop Pattern Prediction API Running!"}