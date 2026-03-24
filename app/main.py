from fastapi import FastAPI
from app.fraud.predict import simple_fraud_check
from app.schemas.fraud import FraudRequest

app = FastAPI(title="Fin-Ops Sentinel")


@app.get("/")
def home():
    return {"message": "Fin-Ops Sentinel API is running"}


@app.post("/predict/fraud")
def predict_fraud(request: FraudRequest):
    risk = simple_fraud_check(request.amount)
    return {
        "amount": request.amount,
        "fraud_risk": risk
    }