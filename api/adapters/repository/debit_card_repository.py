from api.adapters.repository.base_repository import Repository
from api.adapters.repository.interfaces.card_repository_interface import CardRepositoryInterface
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.entities.card.debit_card import DebitCard


class DebitCardRepository(CardRepositoryInterface, Repository):
  
  def __init__(self, db: DatabaseInterface) -> None:
      super().__init__(db=db)
  
  def get_cards(self):
    return self.db.all()
    
  def get_card(self, number: int):
    return self.db.get(field={'number': number})
    
  def create_card(self, debit_card: DebitCard):
    return self.db.create(debit_card)