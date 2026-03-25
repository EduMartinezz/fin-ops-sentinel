import joblib
import pandas as pd


def load_fraud_model():
    model = joblib.load("models/fraud_model.joblib")
    feature_columns = joblib.load("models/fraud_features.joblib")
    return model, feature_columns


def prepare_fraud_features(amount, transaction_type, old_balance_org, new_balance_org, feature_columns):
    input_df = pd.DataFrame([{
        "amount": amount,
        "transaction_type": transaction_type.upper(),
        "old_balance_org": old_balance_org,
        "new_balance_org": new_balance_org,
    }])

    input_df = pd.get_dummies(input_df, columns=["transaction_type"])

    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_columns]
    return input_df