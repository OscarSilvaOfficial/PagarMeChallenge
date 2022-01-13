from abc import ABC, abstractmethod


class TransactionUseCaseInterface(ABC):
  
  @abstractmethod
  def get_transaction(self, transaction_id: int):
    pass

  @abstractmethod
  def get_transactions(self):
    pass
  
  @abstractmethod
  def create_transaction(self, value: float, from_document: str, to_document: str, card_number: int, cvv: int):
    pass