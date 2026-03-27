from app.fraud.model import load_fraud_model, prepare_fraud_features

model, feature_columns = load_fraud_model()


def model_fraud_check(amount, transaction_type, old_balance_org, new_balance_org):
    input_data = prepare_fraud_features(
        amount=amount,
        transaction_type=transaction_type,
        old_balance_org=old_balance_org,
        new_balance_org=new_balance_org,
        feature_columns=feature_columns
    )

    fraud_probability = model.predict_proba(input_data)[0][1]

    if fraud_probability >= 0.7:
        risk = "high_risk"
    elif fraud_probability >= 0.4:
        risk = "medium_risk"
    else:
        risk = "low_risk"

    return risk, fraud_probability


def generate_fraud_reason(amount, transaction_type, fraud_probability):
    reasons = []

    if amount >= 50000:
        reasons.append("high transaction amount")

    if transaction_type.lower() in ["cash_out", "transfer"]:
        reasons.append(f"{transaction_type.lower()} transaction pattern")

    if fraud_probability >= 0.5:
        reasons.append("model detected elevated fraud probability")

    if not reasons:
        return "Transaction shows low fraud indicators."

    return "Risk flagged due to " + ", ".join(reasons) + "."


def generate_risk_factors(amount, transaction_type, fraud_probability):
    factors = {}

    if amount >= 50000:
        factors["amount_risk"] = "high"
    elif amount >= 10000:
        factors["amount_risk"] = "medium"
    else:
        factors["amount_risk"] = "low"

    if transaction_type.lower() in ["cash_out", "transfer"]:
        factors["transaction_pattern"] = "risky"
    else:
        factors["transaction_pattern"] = "normal"

    if fraud_probability >= 0.7:
        factors["model_confidence"] = "high"
    elif fraud_probability >= 0.4:
        factors["model_confidence"] = "medium"
    else:
        factors["model_confidence"] = "low"

    return factors