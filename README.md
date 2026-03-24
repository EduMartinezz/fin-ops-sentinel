# Fin-Ops Sentinel

Fin-Ops Sentinel is a FastAPI-based microservice that simulates real-time financial operations workflows by combining:

- Fraud risk scoring for transaction monitoring
- Sentiment analysis for financial and market-related text
- REST API endpoints for real-time inference

## Features

- `POST /predict/fraud`  
  Predicts fraud risk from transaction data

- `POST /predict/sentiment`  
  Classifies sentiment from financial text

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git & GitHub

## Project Structure

```text
fin-ops-sentinel/
├── app/
│   ├── main.py
│   ├── fraud/
│   │   └── predict.py
│   ├── sentiment/
│   │   └── predict.py
│   └── schemas/
│       ├── fraud.py
│       └── sentiment.py
├── data/
├── models/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md

## Example: Fraud Prediction

Request body:
{
  "text": "The company reported strong profit growth this quarter",
  "sentiment": "positive"
}

## Response:
{
  "text": "The company reported strong profit growth this quarter",
  "sentiment": "positive"
}