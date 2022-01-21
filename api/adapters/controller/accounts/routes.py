from api.useCases.account import AccountUseCase
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.adapters.controller.accounts.parser.account import AccountParser, AccountUpdateParser
from api.infra.http.interfaces.http_api_interface import HttpApiInterface
from api.adapters.repository.account_repository import AccountRepository


def account_routes(router: HttpApiInterface, db: DatabaseInterface, response):
  
  account_use_case = AccountUseCase(account_repository=AccountRepository(db=db))
  
  @router.get('/accounts/', response_model=list[AccountParser])
  async def get_all_accounts():
    return account_use_case.get_accounts()
  
  @router.post('/accounts/', status_code=201)
  async def create_account(account: AccountParser, response: response):
    try:
      return account_use_case.create_account(
        balance=account.balance, 
        document=account.document, 
        user_name=account.user_name
      )
    except Exception as e:
      response.status_code = 409
      return {'message': str(e)}
    
  @router.patch('/accounts/{document}/', status_code=204)
  async def update_account(document: str, account: AccountUpdateParser, response: response):
    try:
      return account_use_case.update_account(document=document, user_name=account.user_name)
    except Exception as e:
      response.status_code = 409
      return {'message': str(e)}