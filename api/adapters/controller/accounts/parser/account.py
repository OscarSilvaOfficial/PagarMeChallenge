from pydantic import BaseModel


class AccountParser(BaseModel):
  document: str
  user_name: str
  balance: float

class AccountUpdateParser(BaseModel):
  user_name: str