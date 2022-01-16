from api.entities.validators.document.interfaces.document_validator_interface import DocumentValidationInterface
from api.entities.interfaces.account_interface import AccountInterface
from api.entities.validators.document.document_validator import DocumentValidator

class Account(AccountInterface):
  
  def __init__(
    self, 
    document: str, 
    user_name: str, 
    balance: float, 
    validator: DocumentValidationInterface=DocumentValidator, 
    id: str=None
  ):
    self._id = id
    self._document = document
    self._user_name = user_name
    self._balance = balance
    validator(document).validate()
    
  @property
  def id(self):
    return self._id

  @property
  def document(self):
    return self._document

  @property
  def user_name(self):
    return self._user_name

  @property
  def balance(self):
    return self._balance

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