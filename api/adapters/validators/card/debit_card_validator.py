from api.adapters.validators.card.card_validator import CardValidator
from api.entities.interfaces.card_interface import CardInterface



class DebitCardValidator(CardValidator):
  
  def __init__(self, card: CardInterface):
    super().__init__(card)
    
  def validate(self):
    self.validate_number()
    self.validate_expire_date()
    self.validate_cvv()