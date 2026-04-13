from pydantic import BaseModel

class PredictionInput(BaseModel):
    # numéricas
    SeniorCitizen: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float

    # categóricas
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
