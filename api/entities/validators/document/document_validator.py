class DocumentValidator:
  
  def __init__(self, document):
    self._document = document

  def validate(self):
    if not self._document:
      raise ValueError('Document is required')
    if len(self._document) != 11:
      raise ValueError('Document must have 11 characters')
    if not self._document.isdigit():
      raise ValueError('Document must have only numbers')