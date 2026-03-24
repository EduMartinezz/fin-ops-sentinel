from fastapi import FastAPI
from app.fraud.predict import simple_fraud_check

app = FastAPI(title="Fin-Ops Sentinel")

@app.get("/")
def home():
    return {"message": "Fin-Ops Sentinel API is running"}

@app.post("/predict/fraud")
def predict_fraud(amount: float):
    risk = simple_fraud_check(amount)
    return {
        "amount": amount,
        "fraud_risk": risk
    }