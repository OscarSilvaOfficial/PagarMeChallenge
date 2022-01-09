from api.adapters.validators.document.interfaces.document_validator_interface import DocumentValidationInterface

class Accout:
  
  def __init__(self, document: str, user_name: str, value: float, validator: DocumentValidationInterface):
    self._document = document
    self._user_name = user_name
    self._value = value
    self.__validator = validator(document)
    self.__validator.validate()

  @property
  def document(self):
    return self._document

  @property
  def user_name(self):
    return self._user_name

  @property
  def value(self):
    return self._value