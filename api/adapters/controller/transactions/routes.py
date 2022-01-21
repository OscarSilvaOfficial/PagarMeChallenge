from api.adapters.controller.transactions.parser.transaction_parser import TransactionParser
from api.useCases.debit_transaction import DebitTransactionsUseCase
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.infra.http.interfaces.http_api_interface import HttpApiInterface
from api.adapters.repository.account_repository import AccountRepository
from api.adapters.repository.transaction_repository import TransactionsRepository


def transaction_routes(router: HttpApiInterface, db: DatabaseInterface, response):
  
  transaction_use_case = DebitTransactionsUseCase(
    transaction_repository=TransactionsRepository(db=db),
    account_repository=AccountRepository(db=db)
  )
  
  @router.get('/transactions/', response_model=list[TransactionParser])
  async def get_all_transactions():
    return transaction_use_case.get_transactions()
  
  @router.post('/transactions/', status_code=201, response_model=TransactionParser)
  async def create_transaction(transaction: TransactionParser, response: response):
    return transaction_use_case.create_transaction(
      from_document=transaction.from_document,
      to_document=transaction.to_document,
      value=transaction.value
    )