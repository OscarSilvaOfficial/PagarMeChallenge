from abc import ABC, abstractmethod
from api.entities.transaction.transaction import Transactions


class TransactionsRepositoryInterface(ABC):

  @abstractmethod
  def get_transactions(self):
    pass

  @abstractmethod
  def get_transaction(self, transaction_id: int):
    pass

  @abstractmethod
  def create_transaction(self, transaction: Transactions):
    pass