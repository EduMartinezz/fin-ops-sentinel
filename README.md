# Fin-Ops Sentinel

Fin-Ops Sentinel is a FastAPI-based microservice that simulates real-time financial operations workflows by combining fraud risk scoring and sentiment analysis into API endpoints.

The project was built to move beyond notebook-based machine learning experiments and toward production-style AI system design.

## Why this project

This project demonstrates how machine learning services can be exposed as structured, reusable APIs for financial operations use cases such as:

- transaction risk scoring
- fraud detection workflows
- financial text sentiment analysis
- real-time inference services

It is designed as a portfolio project that reflects practical engineering skills, including modular code structure, request validation, Git-based development, and Dockerized deployment.

## Features

- **Fraud prediction endpoint**
  - Accepts transaction-style input data
  - Returns a fraud risk label based on simple rule logic

- **Sentiment prediction endpoint**
  - Accepts financial or business-related text
  - Returns a sentiment label: positive, negative, or neutral

- **FastAPI documentation**
  - Interactive API docs available through `/docs`

- **Docker support**
  - Application can be built and run in a containerized environment

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Docker
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
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md

API Endpoints
1. Home endpoint

GET /

Returns a simple health/status message.

Example response:

{
  "message": "Fin-Ops Sentinel API is running"
}

2. Fraud prediction endpoint

POST /predict/fraud

Accepts transaction-style input and returns a fraud risk classification.

Example request
{
  "amount": 120000,
  "transaction_type": "transfer",
  "old_balance_org": 150000,
  "new_balance_org": 30000
}
Example response
{
  "amount": 120000,
  "transaction_type": "transfer",
  "fraud_risk": "high_risk"
}

3. Sentiment prediction endpoint

POST /predict/sentiment

Accepts text input and returns a sentiment classification.

Example request
{
  "text": "The company reported strong profit growth this quarter"
}
Example response
{
  "text": "The company reported strong profit growth this quarter",
  "sentiment": "positive"
}

Running the project locally
1. Clone the repository
git clone https://github.com/EduMartinezz/fin-ops-sentinel.git
cd fin-ops-sentinel

2. Create and activate a virtual environment

On Windows:

python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the FastAPI app
uvicorn app.main:app --reload
5. Open the docs

Open in your browser:

http://127.0.0.1:8000/docs
Running with Docker

1. Build the image
docker build -t fin-ops-sentinel .

2. Run the container
docker run -p 8000:8000 fin-ops-sentinel

3. Open the docs

Open in your browser:

http://127.0.0.1:8000/docs