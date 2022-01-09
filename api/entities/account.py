from api.adapters.validators.document.interfaces.document_validator_interface import DocumentValidationInterface
from api.entities.interfaces.account_interface import AccountInterface

class Accout(AccountInterface):
  
  def __init__(self, document: str, user_name: str, balance: float, validator: DocumentValidationInterface):
    self._document = document
    self._user_name = user_name
    self._balance = balance
    self.validator = validator(document)
    self.validator.validate()

  @property
  def document(self):
    return self._document

  @property
  def user_name(self):
    return self._user_name

  @property
  def balance(self):
    return self._balance
  
  def cashin(self, value: float):
    self._balance += value
    
  def cashout(self, value: float):
    if value > self._balance:
      raise Exception('Not enough cash')
    self._balance -= value