class Transaction:
  
  def __init__(
    self, amount, description, 
    method, card_number, card_name, 
    card_expire_date, card_cvv
  ):
    self._amount = amount
    self._description = description
    self._method = method
    self._card_number = card_number
    self._card_name = card_name
    self._card_expire_date = card_expire_date
    self._card_cvv = card_cvv