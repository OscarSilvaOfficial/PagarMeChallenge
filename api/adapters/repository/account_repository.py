from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.infra.db.interfaces.nosql_interface import NoSQLInterface


class AccountRepository(AccountRepositoryInterface):
  
  def __init__(self, db: NoSQLInterface):
      self.db: NoSQLInterface = db
  
  def get_accounts(self):
    return self.db.all(collection_name='accounts', where={})
    
  def get_account(self, document: int):
    result = self.db.all(collection_name='accounts', where={'document': document})
    return None if not result else result[0]

  def create_account(self, accounts: dict or list[dict]):
    return self.db.create(documents=accounts, collection_name='accounts')