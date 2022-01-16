from api.entities.interfaces.credit_card_interface import CreditCardInterface
from api.entities.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from api.entities.validators.card.credit_card_validator import CreditCardValidator
from .card import Card 


class CreditCard(Card, CreditCardInterface):
  
  def __init__(
    self, 
    number: int, 
    client_name: str, 
    expire_date: str, 
    cvv: int, 
    credit_limit,
    validator: CardValidatorInterface=CreditCardValidator, 
    id: int=None,
    type: str = 'debit_card',
  ):
    super().__init__(id, number, client_name, expire_date, cvv, type, validator)
    self._credit_limit = credit_limit
    
  def validate(self):
    self.validator.validate()
    
  @property
  def credit_limit(self):
    return self._credit_limit
  
  def cashout(self, value):
    if self.credit_limit < value:
      raise Exception('Credit limit exceeded')
    self._credit_limit -= value