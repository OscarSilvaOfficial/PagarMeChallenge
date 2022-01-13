from api.entities.interfaces.account_interface import AccountInterface
from api.entities.interfaces.card_interface import CardInterface
from api.entities.interfaces.credit_card_interface import CreditCardInterface


class Transaction:
  
  def __init__(
    self, 
    description: str,
    from_account: AccountInterface, 
    to_account: AccountInterface, 
    card: CardInterface
  ):
    self._description = description
    self._from_account = from_account
    self._to_account = to_account
    self._card = card
  
  @property
  def description(self):
    return self._description
  
  @property
  def from_account(self):
    return self._from_account
  
  @property
  def to_account(self):
    return self._to_account
  
  @property
  def card(self):
    return self._card
    
  def validate(self):
    if self._card.type is not 'debit_card':
      raise Exception('Invalid card type')
    self._card.validate()