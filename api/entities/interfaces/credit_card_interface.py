from abc import abstractmethod
from .card_interface import CardInterface


class CreditCardInterface(CardInterface):
  
  @abstractmethod
  def cashout(self, value):
    pass