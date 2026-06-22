from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

model_package = r"C:/Users/jenifer/Downloads/XGB/XGBoost_Model/crop_pattern_model_XGB.joblib"


package = joblib.load(model_package)
mean_model = package["mean_model"]
median_model = package["median_model"]

valid_values = package["valid_values"]

app = FastAPI(title="Crop Pattern API")

method = input(
    "Enter method (mean/median): "
).lower().strip()

if method not in ["mean", "median"]:
    print("Method must be mean or median")
    exit()

model = (
    package["mean_model"]
    if method == "mean"
    else package["median_model"]
)

valid_values = package["valid_values"]


def validate_input(
    crop,
    season,
    state,
    valid_values
):
    crop = crop.lower().strip()
    season = season.lower().strip()
    state = state.lower().strip()

    if crop not in valid_values["crops"]:
        raise ValueError(
            "Invalid crop"
        )

    if season not in valid_values["seasons"]:
        raise ValueError(
            "Invalid season"
        )

    if state not in valid_values["states"]:
        raise ValueError(
            "Invalid state"
        )

    return crop, season, state


try:

    crop = input(
        "Enter Crop Name: "
    ).lower().strip()

    year = int(
        input(
            "Enter Year: "
        )
    )

    season = input(
        "Enter Season: "
    ).lower().strip()

    state = input(
        "Enter State: "
    ).lower().strip()

    area = float(
        input(
            "Enter Area: "
        )
    )

    yield_val = float(
        input(
            "Enter Yield: "
        )
    )

    crop, season, state = validate_input(
        crop,
        season,
        state,
        valid_values
    )

    new_data = pd.DataFrame({
        "crop": [crop],
        "crop_year": [year],
        "season": [season],
        "state": [state],
        "area": [area],
        "yield": [yield_val]
    })
   
    score = float(
        model.predict(
            new_data
        )[0]
    )


    print("INPUT:")
    print(new_data)

    print("PREDICTED SCORE:")
    print(score)
    
    score = max(
        0,
        min(score, 100)
    )

    if score >= 70:
        status = "Great cropping pattern"

    elif score >= 60:
        status = "Good cropping pattern"

    elif score >= 40:
        status = "Average cropping pattern"

    else:
        status = "Bad cropping pattern"

    print(
        f"\nCropping Pattern Score: {score:.2f}%"
    )

    print(
        f"Status: {status}"
    )

    result = {
        "raw_score": score,
        "cropping_pattern_score": round(score, 2),
        "status": status
    }
    print(result)
except Exception as e:

    print(
        f"Error: {e}"
    )