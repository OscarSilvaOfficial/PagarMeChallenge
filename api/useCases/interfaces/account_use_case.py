from abc import ABC, abstractmethod


class AccountUseCaseInterface(ABC):
  
  @abstractmethod
  def get_account(self, account_id: int):
    pass

  @abstractmethod
  def get_accounts(self):
    pass
  
  @abstractmethod
  def create_account(self, document: str, user_name: str, balance: float):
    pass