from api.entities.interfaces.account_interface import AccountInterface
from .transaction import Transactions


class DebitTransactions(Transactions):
  
  def __init__(
    self, 
    value: float,
    description: str,
    from_account: AccountInterface, 
    to_account: AccountInterface, 
  ):
    super().__init__(value, description, from_account, to_account)
  