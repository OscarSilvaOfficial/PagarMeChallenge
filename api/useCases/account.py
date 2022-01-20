from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.entities.account.account import Account
from api.useCases.interfaces.account_use_case import AccountUseCaseInterface

class AccountUseCase(AccountUseCaseInterface):
  
  def __init__(
    self, 
    account_repository: AccountRepositoryInterface,
  ):
    self._account_repository = account_repository
    
  def _validate_if_account_exists(self, document: str):
    account = self._account_repository.get_account(document=document)
    if account:
      return True
    return False
  
  def get_accounts(self):
    return self._account_repository.get_accounts()
  
  def get_account(self, document: int):
    return self._account_repository.get_account(transaction_id=document)

  def create_account(self, document: str, user_name: str, balance: float):
    
    if self._validate_if_account_exists(document=document):
      raise Exception('Account already exists')
    
    account = Account(balance=balance, document=document, user_name=user_name)
    return self._account_repository.create_account(accounts=account.to_dict())

      