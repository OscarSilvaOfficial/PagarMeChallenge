from api.adapters.repository.base_repository import Repository
from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.entities.account.account import Account


class AccountRepository(AccountRepositoryInterface, Repository):
  
  def __init__(self, db: DatabaseInterface) -> None:
      super().__init__(db=db)
  
  def get_accounts(self):
    return self.db.all()
    
  def get_account(self, document: int):
    return self.db.get(document)
    
  def create_account(self, account: Account):
    return self.db.create(account)