from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.adapters.repository.interfaces.transaction_repository_interface import TransactionsRepositoryInterface
from api.entities.transaction.dabit_transaction import DebitTransactions
from api.useCases.interfaces.debit_transaction_use_case import DebitTransactionsUseCaseInterface
from api.entities.account.account import Account


class DebitTransactionsUseCase(DebitTransactionsUseCaseInterface):
  
  def __init__(
    self, 
    transaction_repository: TransactionsRepositoryInterface, 
    account_repository: AccountRepositoryInterface,
  ):
    self._transaction_repository = transaction_repository
    self._account_repository = account_repository
    
  def _replace_id_key(self, entity: dict):
    entity['id'] = entity['_id']
    entity.pop('_id')
  
  def get_transactions(self):
    return self._transaction_repository.get_transactions()
  
  def get_transaction(self, transaction_id: int):
    return self._transaction_repository.get_transaction(transaction_id=transaction_id)

  def create_transaction(self, value: float, from_document: str, to_document: str):
    from_account_data = self._account_repository.get_account(document=from_document)
    to_account_data = self._account_repository.get_account(document=to_document)
    
    for account_data in [from_account_data, to_account_data]:
      self._replace_id_key(account_data)
        
    from_account = Account(**from_account_data)
    to_account = Account(**to_account_data)
    
    from_account.cashout(value)
    to_account.cashin(value)

    transaction = DebitTransactions(
      description='Debit transaction',
      from_account=from_account.document,
      to_account=to_account.document,
      value=value
    )
            
    return self._transaction_repository.create_transaction(transaction=transaction.to_dict())
      