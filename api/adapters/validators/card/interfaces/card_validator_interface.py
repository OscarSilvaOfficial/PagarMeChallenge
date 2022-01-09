from abc import ABC, abstractmethod


class CardValidatorInterface(ABC):
    
  @abstractmethod
  def validate(self):
    pass