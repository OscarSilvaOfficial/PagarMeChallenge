from api.entities.interfaces.credit_card_interface import CreditCardInterface
from api.entities.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from .card import Card 


class CreditCard(Card, CreditCardInterface):
  
  def __init__(self, number: int, client_name: str, expire_date: str, cvv: int, validator: CardValidatorInterface, credit_limit):
    super().__init__(number, client_name, expire_date, cvv, 'credit_card', validator)
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