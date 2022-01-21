from typing import Optional
from pydantic import BaseModel


class TransactionParser(BaseModel):
  from_document: str 
  to_document: str
  value: float
  description: Optional[str] = None
