from api.adapters.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from api.entities.interfaces.card_interface import CardInterface
from datetime import datetime



class CardValidator(CardValidatorInterface):
  def __init__(self, card: CardInterface):
    self.card = card
    
  def validate_name(self):
    if self.card.client_name is None:
      raise Exception('Invalid name')

  def validate_number(self):
    if len(self.card.number) > 16:
      raise Exception('Invalid number')
    
  def validate_expire_date(self):
    day, month, year = self.card.expire_date.split('/')
    expire_date = datetime(year, month, day)
    if expire_date < datetime.now():
      raise Exception('Invalid expire date')
    
  def validate_cvv(self):
    if len(self.card.cvv) > 3:
      raise Exception('Invalid cvv')