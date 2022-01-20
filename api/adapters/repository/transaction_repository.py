from api.adapters.repository.interfaces.transaction_repository_interface import TransactionsRepositoryInterface
from api.infra.db.interfaces.sql_interface import DatabaseInterface


class TransactionsRepository(TransactionsRepositoryInterface):
  
  def __init__(self, db: DatabaseInterface) -> None:
      super().__init__(db=db)
  
  def get_transactions(self):
    return self.db.all()
    
  def get_transaction(self, id: int):
    return self.db.get(where={ 'id': id })
    
  def create_transaction(self, transaction):
    return self.db.create(transaction)