def simple_fraud_check(amount: float):
    if amount > 10000:
        return "high_risk"
    elif amount > 5000:
        return "medium_risk"
    else:
        return "low_risk"