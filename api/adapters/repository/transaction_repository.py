from api.adapters.repository.base_repository import Repository
from api.adapters.repository.interfaces.transaction_repository_interface import TransactionRepositoryInterface
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.entities.transaction.dabit_transaction import DebitTransaction


class TransactionRepository(TransactionRepositoryInterface, Repository):
  
  def __init__(self, db: DatabaseInterface) -> None:
      super().__init__(db=db, entity=DebitTransaction)
  
  def get_transactions(self):
    return self.db.all()
    
  def get_transaction(self, id: int):
    return self.db.get(id)
    
  def create_transaction(self, debit_transaction: DebitTransaction):
    return self.db.create(debit_transaction)