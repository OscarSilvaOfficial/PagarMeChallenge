from abc import ABC, abstractmethod


class HttpApiInterface(ABC):
  
  @abstractmethod
  def get(self):
    pass

  @abstractmethod
  def post(self):
    pass
  
  @abstractmethod
  def put(self):
    pass
  
  @abstractmethod
  def patch(self):
    pass
  
  @abstractmethod
  def delete(self):
    pass