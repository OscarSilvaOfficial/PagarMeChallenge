from api.entities.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from .card import Card 


class DebitCard(Card):
  
  def __init__(self, number: int, client_name: str, expire_date: str, cvv: int, validator: CardValidatorInterface):
    super().__init__(number, client_name, expire_date, cvv, 'debit_card', validator)
  
  def validate(self):
    self.validator.validate()