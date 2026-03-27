from fastapi import FastAPI
from app.schemas.fraud import FraudRequest
from app.sentiment.predict import finbert_sentiment_check
from app.schemas.sentiment import SentimentRequest
from app.sentiment.model import preload_finbert, get_finbert_error
from app.fraud.predict import model_fraud_check,generate_fraud_reason,generate_risk_factors

app = FastAPI(
    title="Fin-Ops Sentinel API",
    description="AI-powered financial risk monitoring API for fraud detection and sentiment analysis.",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    preload_finbert()


@app.get("/")
def home():
    return {
        "project": "Fin-Ops Sentinel API",
        "status": "running",
        "features": [
            "fraud detection",
            "fraud explanation generation",
            "financial sentiment analysis"
        ],
        "docs_url": "/docs"
    }


@app.get("/health/sentiment")
def sentiment_health():
    error = get_finbert_error()
    return {
        "finbert_loaded": error is None,
        "finbert_error": error
    }


@app.post("/predict/fraud")
def predict_fraud(request: FraudRequest):
    risk, fraud_probability = model_fraud_check(
        amount=request.amount,
        transaction_type=request.transaction_type,
        old_balance_org=request.old_balance_org,
        new_balance_org=request.new_balance_org,
    )

    reason = generate_fraud_reason(
        amount=request.amount,
        transaction_type=request.transaction_type,
        fraud_probability=fraud_probability
    )

    risk_factors = generate_risk_factors(
        amount=request.amount,
        transaction_type=request.transaction_type,
        fraud_probability=fraud_probability
    )

    return {
        "amount": request.amount,
        "transaction_type": request.transaction_type,
        "fraud_risk": risk,
        "fraud_probability": round(fraud_probability, 4),
        "reason": reason,
        "risk_factors": risk_factors
    }

@app.post("/predict/sentiment")
def predict_sentiment(request: SentimentRequest):
    sentiment, confidence, source = finbert_sentiment_check(request.text)

    return {
        "text": request.text,
        "sentiment": sentiment,
        "confidence": round(confidence, 4) if confidence is not None else None,
        "source": source
    }