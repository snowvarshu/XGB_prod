# Crop Pattern Prediction System

## Overview

The Crop Pattern Prediction System is a Machine Learning-powered web application that evaluates agricultural cropping performance and generates a cropping pattern score based on historical crop production data.

The system uses XGBoost Regression models trained on crop production datasets and provides predictions through a FastAPI backend and Angular frontend.

---

## Features

* Predict Crop Pattern Score
* Mean-based scoring model
* Median-based scoring model
* FastAPI REST API
* Angular Frontend
* Dockerized Deployment
* Docker Hub Integration
* Production-ready Architecture

---

## Project Architecture

Frontend (Angular)

↓

FastAPI Backend

↓

XGBoost Models

↓

Crop Dataset & Feature Engineering

---

## Technologies Used

### Frontend

* Angular
* TypeScript
* HTML
* CSS

### Backend

* FastAPI
* Python
* Pandas
* NumPy

### Machine Learning

* XGBoost Regressor
* Scikit-Learn
* Joblib

### Deployment

* Docker
* Docker Hub

---

## Input Parameters

The model accepts the following inputs:

| Field      | Type          |
| ---------- | ------------- |
| Crop       | String        |
| Crop Year  | Integer       |
| Season     | String        |
| State      | String        |
| Area       | Float         |
| Production | Float         |
| Method     | Mean / Median |

Example:

```json
{
  "crop": "rice",
  "crop_year": 2026,
  "season": "kharif",
  "state": "tamil nadu",
  "area": 100,
  "production": 300,
  "method": "mean"
}
```

---

## Output

Example Response:

```json
{
  "cropping_pattern_score": 76.42,
  "status": "Great cropping pattern"
}
```

### Score Interpretation

| Score Range | Status                   |
| ----------- | ------------------------ |
| 70+         | Great Cropping Pattern   |
| 60 - 69     | Good Cropping Pattern    |
| 40 - 59     | Average Cropping Pattern |
| Below 40    | Bad Cropping Pattern     |

---

## Machine Learning Pipeline

### Feature Engineering

The following features are generated:

* Production per Area
* Baseline Production
* Baseline Area
* Production Ratio
* Area Ratio
* Productivity Ratio

### Models

The project contains three trained XGBoost models:

1. Main Cropping Pattern Score Model
2. Mean-Based Score Model
3. Median-Based Score Model

### Performance

Current Model Performance:

* MAE: ~1.69
* RMSE: ~7.37
* R² Score: ~0.77

---

## Backend Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run Angular application:

```bash
ng serve
```

Frontend URL:

```text
http://localhost:4200
```

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t crop-score-api .
```

### Run Container

```bash
docker run -p 8000:8000 crop-score-api
```

---

## Docker Hub

### Tag Image

```bash
docker tag crop-score-api vsnowvarshini/crop-score-api:v1
```

### Push Image

```bash
docker push vsnowvarshini/crop-score-api:v1
```

### Pull Image

```bash
docker pull vsnowvarshini/crop-score-api:v1
```

### Run Pulled Image

```bash
docker run -d -p 8000:8000 vsnowvarshini/crop-score-api:v1
```

---

## API Endpoint

### POST /predict

Endpoint:

```text
POST /predict
```

Request Body:

```json
{
  "crop": "rice",
  "crop_year": 2026,
  "season": "kharif",
  "state": "tamil nadu",
  "area": 100,
  "production": 300,
  "method": "mean"
}
```

---

## Future Improvements

* Weather-based prediction
* Soil quality integration
* Satellite data integration
* Multi-crop recommendation engine
* Cloud deployment
* Real-time agricultural analytics dashboard

---

## Author

Snow Varshini

Machine Learning Engineer | AI & ML Enthusiast

---

## License

This project is developed for educational and research purposes.
