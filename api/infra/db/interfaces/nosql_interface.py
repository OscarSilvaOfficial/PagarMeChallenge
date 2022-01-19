from abc import ABC, abstractmethod


class NoSQLInterface(ABC):
  
  @abstractmethod
  def all(self, collection_name, where):
    pass
  
  @abstractmethod
  def create(self, collection_name, documents):
    pass
  
  @abstractmethod
  def delete(self, collection_name, where):
    pass