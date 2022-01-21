class Transactions:
  
  def __init__(
    self, 
    value: float,
    description: str,
    from_document: str, 
    to_document: str, 
  ):
    self._value = value
    self._description = description
    self._from_document = from_document
    self._to_document = to_document
    
  @property
  def value(self):
    return self._value
  
  @property
  def description(self):
    return self._description
  
  @property
  def from_document(self):
    return self._from_document
  
  @property
  def to_document(self):
    return self._to_document
  
  def to_dict(self):
    return {
      'value': self._value,
      'description': self._description,
      'from_document': self._from_document,
      'to_document': self._to_document
    }
    