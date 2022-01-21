from api.adapters.repository.interfaces.transaction_repository_interface import TransactionsRepositoryInterface
from api.infra.db.interfaces.nosql_interface import NoSQLInterface


class TransactionsRepository(TransactionsRepositoryInterface):
  
  def __init__(self, db: NoSQLInterface) -> None:
    self.db = db
  
  def get_transactions(self):
    return self.db.all(collection_name='transactions')
    
  def get_transaction(self, id: int):
    return self.db.all(collection_name='transactions', where={ 'id': id })
    
  def create_transaction(self, transaction):
    try:
      self.db.create(collection_name='transactions', documents=transaction)
      return transaction
    except Exception:
      return Exception('Erro ao criar transação')
