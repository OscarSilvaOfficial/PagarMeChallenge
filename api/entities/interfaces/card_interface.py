from abc import ABC, abstractmethod

class CardInterface(ABC):
  
  @abstractmethod
  def number(self):
    pass
  
  @abstractmethod
  def client_name(self):
    pass
  
  @abstractmethod
  def expire_date(self):
    pass
  
  @abstractmethod
  def cvv(self):
    pass
  
  @abstractmethod
  def type(self):
    pass
  
  @abstractmethod
  def validate(self):
    pass