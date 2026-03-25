import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset (adjust filename if needed)
file_path = "data/paysim dataset.csv"

print("Loading dataset...")

# Load only required columns (important!)
data = pd.read_csv(
    file_path,
    usecols=["amount", "type", "oldbalanceOrg", "newbalanceOrig", "isFraud"],
    nrows=100000  # LIMIT rows to avoid memory crash
)

print("Dataset loaded:", data.shape)

# Rename columns for consistency
data = data.rename(columns={
    "type": "transaction_type",
    "oldbalanceOrg": "old_balance_org",
    "newbalanceOrig": "new_balance_org",
    "isFraud": "is_fraud"
})

# One-hot encoding
X = pd.get_dummies(
    data[["amount", "transaction_type", "old_balance_org", "new_balance_org"]],
    columns=["transaction_type"]
)

y = data["is_fraud"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
print("Training model...")
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.4f}")

# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/fraud_model.joblib")
joblib.dump(list(X.columns), "models/fraud_features.joblib")

print("Model saved successfully.")