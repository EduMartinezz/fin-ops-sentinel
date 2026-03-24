from fastapi import FastAPI
from app.fraud.predict import simple_fraud_check
from app.schemas.fraud import FraudRequest

app = FastAPI(title="Fin-Ops Sentinel")


@app.get("/")
def home():
    return {"message": "Fin-Ops Sentinel API is running"}


@app.post("/predict/fraud")
def predict_fraud(request: FraudRequest):
    risk = simple_fraud_check(
        amount=request.amount,
        transaction_type=request.transaction_type,
        old_balance_org=request.old_balance_org,
        new_balance_org=request.new_balance_org,
    )

    return {
        "amount": request.amount,
        "transaction_type": request.transaction_type,
        "fraud_risk": risk
    }