from abc import ABC, abstractmethod


class CreditTransactionUseCaseInterface(ABC):
  
  @abstractmethod
  def get_transaction(self, transaction_id: int):
    pass

  @abstractmethod
  def get_transactions(self):
    pass
  
  @abstractmethod
  def create_transaction(self):
    pass