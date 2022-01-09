from .interfaces.card_interface import CardInterface
from abc import abstractmethod


class Card(CardInterface):
  
  def __init__(self, number, client_name, expire_date, cvv, type, validator):
    self._number = number
    self._client_name = client_name
    self._expire_date = expire_date
    self._cvv = cvv
    self._type = type
    self.validator = validator(self)
  
  @property  
  def number(self):
    return self._number
  
  @property
  def client_name(self):
    return self._client_name
    
  @property
  def expire_date(self):
    return self._expire_date
    
  @property
  def cvv(self):
    return self._cvv
  
  @property
  def type(self):
    return self._type