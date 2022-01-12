from api.adapters.repository.interfaces.transaction_repository import TransactionRepositoryInterface
from api.entities.account import Account
from api.useCases.interfaces.debit_transaction_use_case import DebitTransactionUseCaseInterface


class DebitTransaction(DebitTransactionUseCaseInterface):
  
  def __init__(self, transaction_repository: TransactionRepositoryInterface):
    self._transaction_repository = transaction_repository
  
  def get_transactions(self):
    return self._transaction_repository.get_transactions()
  
  def get_transaction(self, transaction_id: int):
    return self._transaction_repository.get_transaction(transaction_id=transaction_id)

  def create_transaction(self, value: float, from_document: str, to_document: str, card_number: int, cvv: int):
    # TODO: Implement this method
    pass