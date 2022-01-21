from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.infra.db.interfaces.nosql_interface import NoSQLInterface


class AccountRepository(AccountRepositoryInterface):
  
  def __init__(self, db: NoSQLInterface):
      self.db: NoSQLInterface = db
      self._collection_name = 'accounts'
  
  def get_accounts(self):
    return self.db.all(collection_name=self._collection_name, where={})
    
  def get_account(self, document: int):
    result = self.db.all(collection_name=self._collection_name, where={'document': document})
    return None if not result else result[0]

  def create_account(self, accounts):
    try:
      self.db.create(documents=accounts, collection_name=self._collection_name)
      return "Conta cliente criada com sucesso"
    except Exception:
      return Exception('Erro ao criar conta')
    
  def update_account(self, document: str, update_values: dict):
    try:
      self.db.update(collection_name=self._collection_name, where={'document': document}, new_values=update_values)
      return "Conta atualizada com sucesso"
    except Exception:
      return Exception('Erro ao atualizar conta')