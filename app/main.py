from fastapi import FastAPI
from app.model import load_model, predict
from app.schemas import PredictionInput
app = FastAPI(title="Modelo Churn API")
@app.on_event("startup")
def startup_event():
    load_model()
@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}
@app.post("/predict")
def make_prediction(input_data: PredictionInput):

    data = [
        input_data.SeniorCitizen,
        input_data.tenure,
        input_data.MonthlyCharges,
        input_data.TotalCharges,

        input_data.gender,
        input_data.Partner,
        input_data.Dependents,
        input_data.PhoneService,
        input_data.MultipleLines,
        input_data.InternetService,
        input_data.OnlineSecurity,
        input_data.OnlineBackup,
        input_data.DeviceProtection,
        input_data.TechSupport,
        input_data.StreamingTV,
        input_data.StreamingMovies,
        input_data.Contract,
        input_data.PaperlessBilling,
        input_data.PaymentMethod
    ]

    result = predict(data)

    return {"prediction": result.tolist()}
