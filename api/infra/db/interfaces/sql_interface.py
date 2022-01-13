from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
  
  @abstractmethod
  def all(self):
    pass
  
  @abstractmethod
  def get(self, id: int):
    pass
  
  @abstractmethod
  def create(self, entity):
    pass
  
  @abstractmethod
  def update(self, id: int, entity):
    pass
  
  @abstractmethod
  def delete(self, id: int):
    pass