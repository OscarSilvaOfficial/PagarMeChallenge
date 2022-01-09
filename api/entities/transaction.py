from api.entities.interfaces.account_interface import AccountInterface
from api.entities.interfaces.card_interface import CardInterface
from api.entities.interfaces.credit_card_interface import CreditCardInterface


class Transaction:
  
  def __init__(self, description: str):
    self._description = description
    
  def create_debit_transaction(self, value: float, from_account: AccountInterface, to_account: AccountInterface, card: CardInterface):
    
    if card.type is not 'debit_card':
      raise Exception('Invalid card type')
    
    card.validate()
    
    from_account.cashout(value)
    to_account.cashin(value)
    
    return "Transaction created"
  
  def create_credit_transaction(self, value: float, to_account: AccountInterface, card: CreditCardInterface):
    
    if card.type is not 'credit_card':
      raise Exception('Invalid card type')
    
    card.validate()
    
    card.cashout(value)
    to_account.cashin(value)
    
    return "Transaction created"