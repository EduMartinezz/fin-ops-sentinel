def simple_fraud_check(
    amount: float,
    transaction_type: str,
    old_balance_org: float,
    new_balance_org: float
):
    transaction_type = transaction_type.upper()

    if transaction_type == "TRANSFER" and amount > 10000:
        return "high_risk"
    if old_balance_org > 0 and new_balance_org == 0 and amount > 5000:
        return "medium_risk"
    return "low_risk"