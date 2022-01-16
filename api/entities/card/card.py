from api.entities.validators.card.interfaces.card_validator_interface import CardValidatorInterface
from ..interfaces.card_interface import CardInterface


class Card(CardInterface):
  
  def __init__(self, id: int, number: int, client_name: str, expire_date: str, cvv: int, type: str, validator: CardValidatorInterface):
    self._id = id
    self._number = number
    self._client_name = client_name
    self._expire_date = expire_date
    self._cvv = cvv
    self._type = type
    self.validator = validator(self)
  
  @property
  def id(self):
    return self._id
  
  @property  
  def number(self):
    return self._number
  
  @property
  def client_name(self):
    return self._client_name
    
  @property
  def expire_date(self):
    return self._expire_date
    
  @property
  def cvv(self):
    return self._cvv
  
  @property
  def type(self):
    return self._type