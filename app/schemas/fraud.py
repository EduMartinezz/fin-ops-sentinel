from pydantic import BaseModel


class FraudRequest(BaseModel):
    amount: float