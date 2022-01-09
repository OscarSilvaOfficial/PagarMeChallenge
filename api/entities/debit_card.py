from .card import Card 


class DebitCard(Card):
  
  def __init__(self, number, client_name, expire_date, cvv, validator):
    super().__init__(number, client_name, expire_date, cvv, 'debit_card', validator)
  
  def validate(self):
    self.validator.validate()