from abc import ABC, abstractmethod

class DocumentValidationInterface(ABC):
  
  @abstractmethod
  def validate(self):
    pass