from api.entities.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from api.entities.validators.card.debit_card_validator import DebitCardValidator
from .card import Card 


class DebitCard(Card):
  
  def __init__(
    self, 
    number: int, 
    client_name: str, 
    expire_date: str, 
    cvv: int, 
    validator: CardValidatorInterface=DebitCardValidator, 
    id: int=None,
    type: str = 'debit_card',
  ):
    super().__init__(id, number, client_name, expire_date, cvv, type, validator)
  
  def validate(self):
    self.validator.validate()