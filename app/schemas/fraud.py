from pydantic import BaseModel


class FraudRequest(BaseModel):
    amount: float
    transaction_type: str
    old_balance_org: float
    new_balance_org: float