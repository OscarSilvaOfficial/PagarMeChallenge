from api.adapters.repository.interfaces.card_repository_interface import CardRepositoryInterface
from api.infra.db.interfaces.sql_interface import DatabaseInterface


class DebitCardRepository(CardRepositoryInterface):
  
  def __init__(self, db: DatabaseInterface) -> None:
      super().__init__(db=db)
  
  def get_cards(self):
    return self.db.all()
    
  def get_card(self, number: int):
    return self.db.all(where={'number': number})
    
  def create_card(self, debit_card):
    return self.db.create(debit_card)