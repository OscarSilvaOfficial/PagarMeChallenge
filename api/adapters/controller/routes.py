from api.entities.account.account import Account
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.infra.http.interfaces.http_api_interface import HttpApiInterface
from api.adapters.repository.account_repository import AccountRepository
from api.useCases.account import AccountUseCase
from .parser.account import AccountParser



def main_routes(router: HttpApiInterface, db: DatabaseInterface):
  
  account_use_case = AccountUseCase(account_repository=AccountRepository(db=db))
  
  @router.get('/')
  async def index():
    return {'message': 'Hello World'}
  
  @router.get('/accounts/', response_model=list[AccountParser])
  async def get_all_accounts():
    return account_use_case.get_accounts()
  
  @router.post('/accounts/', status_code=201)
  async def create_account(account: AccountParser):
    return account_use_case.create_account(
      balance=account.balance, 
      document=account.document, 
      user_name=account.user_name
    )
  
  return router
