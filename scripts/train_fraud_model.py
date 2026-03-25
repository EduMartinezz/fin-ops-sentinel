import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Small synthetic training data for proof of pipeline
data = pd.DataFrame([
    {"amount": 200, "transaction_type": "PAYMENT", "old_balance_org": 5000, "new_balance_org": 4800, "is_fraud": 0},
    {"amount": 150000, "transaction_type": "TRANSFER", "old_balance_org": 200000, "new_balance_org": 50000, "is_fraud": 1},
    {"amount": 80000, "transaction_type": "CASH_OUT", "old_balance_org": 90000, "new_balance_org": 0, "is_fraud": 1},
    {"amount": 300, "transaction_type": "DEBIT", "old_balance_org": 1000, "new_balance_org": 700, "is_fraud": 0},
    {"amount": 10000, "transaction_type": "TRANSFER", "old_balance_org": 50000, "new_balance_org": 40000, "is_fraud": 0},
    {"amount": 120000, "transaction_type": "TRANSFER", "old_balance_org": 150000, "new_balance_org": 30000, "is_fraud": 1},
])

# One-hot encode transaction type
X = pd.get_dummies(
    data[["amount", "transaction_type", "old_balance_org", "new_balance_org"]],
    columns=["transaction_type"]
)
y = data["is_fraud"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/fraud_model.joblib")
joblib.dump(list(X.columns), "models/fraud_features.joblib")

print("Fraud model and feature columns saved successfully.")