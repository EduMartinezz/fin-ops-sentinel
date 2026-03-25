from fastapi import FastAPI
from app.fraud.predict import model_fraud_check
from app.schemas.fraud import FraudRequest
from app.sentiment.predict import simple_sentiment_check
from app.schemas.sentiment import SentimentRequest

app = FastAPI(title="Fin-Ops Sentinel")


@app.get("/")
def home():
    return {"message": "Fin-Ops Sentinel API is running"}


@app.post("/predict/fraud")
def predict_fraud(request: FraudRequest):
    risk = model_fraud_check(
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


@app.post("/predict/sentiment")
def predict_sentiment(request: SentimentRequest):
    sentiment = simple_sentiment_check(request.text)

    return {
        "text": request.text,
        "sentiment": sentiment
    }