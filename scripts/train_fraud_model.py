import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Load dataset
file_path = "data/paysim dataset.csv"

print("Loading dataset...")

data = pd.read_csv(
    file_path,
    usecols=["amount", "type", "oldbalanceOrg", "newbalanceOrig", "isFraud"],
    nrows=100000
)

print("Dataset loaded:", data.shape)

# Rename columns
data = data.rename(columns={
    "type": "transaction_type",
    "oldbalanceOrg": "old_balance_org",
    "newbalanceOrig": "new_balance_org",
    "isFraud": "is_fraud"
})

# Feature engineering
data["balance_diff"] = data["old_balance_org"] - data["new_balance_org"]

# Prepare features
X = pd.get_dummies(
    data[["amount", "transaction_type", "old_balance_org", "new_balance_org", "balance_diff"]],
    columns=["transaction_type"]
)

y = data["is_fraud"]

print("\nFraud label counts:")
print(y.value_counts())

# Stratify keeps fraud ratio similar in train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining model...")
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fraud_model.joblib")
joblib.dump(list(X.columns), "models/fraud_features.joblib")

print("\nModel and feature columns saved successfully.")