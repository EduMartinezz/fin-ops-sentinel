from app.fraud.model import load_fraud_model, prepare_fraud_features

model, feature_columns = load_fraud_model()


def model_fraud_check(amount, transaction_type, old_balance_org, new_balance_org):
    features = prepare_fraud_features(
        amount=amount,
        transaction_type=transaction_type,
        old_balance_org=old_balance_org,
        new_balance_org=new_balance_org,
        feature_columns=feature_columns,
    )

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    risk_label = "high_risk" if prediction == 1 else "low_risk"

    return risk_label, float(probability)