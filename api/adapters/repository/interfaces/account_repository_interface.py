from abc import ABC, abstractmethod
from api.entities.account.account import Account


class AccountRepositoryInterface(ABC):
  
  @abstractmethod
  def get_accounts(self):
    pass

  @abstractmethod
  def get_account(self, document: int):
    pass

  @abstractmethod
  def create_account(self, account: Account):
    pass
