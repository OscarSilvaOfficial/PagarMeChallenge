from api.entities.interfaces.account_interface import AccountInterface
from api.entities.interfaces.card_interface import CardInterface
from .transaction import Transactions


class DebitTransactions(Transactions):
  
  def __init__(
    self, 
    description: str,
    from_account: AccountInterface, 
    to_account: AccountInterface, 
    card: CardInterface
  ):
    super().__init__(description, from_account, to_account, card)
    self.validate()
    
  def validate(self):
    if self._card.type is not 'debit_card':
      raise Exception('Invalid card type')
    self._card.validate()