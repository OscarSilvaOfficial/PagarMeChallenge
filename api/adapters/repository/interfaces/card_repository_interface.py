from abc import ABC, abstractmethod
from api.entities.card.card import Card


class CardRepositoryInterface(ABC):
  
  @abstractmethod
  def get_cards(self):
    pass

  @abstractmethod
  def get_card(self, number: int, cvv: int):
    pass

  @abstractmethod
  def create_card(self, card: Card):
    pass
