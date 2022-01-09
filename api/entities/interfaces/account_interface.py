from abc import ABC, abstractmethod


class AccountInterface(ABC):
  
  @abstractmethod
  def document(self):
    pass

  @abstractmethod
  def user_name(self):
    pass

  @abstractmethod
  def balance(self):
    pass
  
  @abstractmethod
  def cashin(self, value: float):
    pass
  
  @abstractmethod
  def cashout(self, value: float):
    pass
