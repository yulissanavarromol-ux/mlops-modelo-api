import joblib
from pathlib import Path

model = None

def load_model():
    global model
    base_dir = Path(__file__).resolve().parent.parent
    model_path = base_dir / "models" / "modelo_v1.joblib"
    model = joblib.load(model_path)

import pandas as pd

def predict(data):
    columns = [
        "SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges",
        "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
        "PaperlessBilling", "PaymentMethod"
    ]

    df = pd.DataFrame([data], columns=columns)

    return model.predict(df)
