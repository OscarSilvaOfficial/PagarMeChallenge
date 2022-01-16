from api.entities.transaction.transaction import Transactions
from api.infra.db.sqlite import SQLite
from api.useCases.debit_transaction import DebitTransactionsUseCase
from api.entities.account.account import Account
from api.entities.card.debit_card import DebitCard
from api.adapters.repository.account_repository import AccountRepository
from api.adapters.repository.debit_card_repository import DebitCardRepository
from api.adapters.repository.transaction_repository import TransactionsRepository


def test_transaction():
  SQLite(db_name='test.db')._create_tables()
  accout_repository = AccountRepository(db=SQLite(db_name='test.db', entity=Account))
  debit_card_repository = DebitCardRepository(db=SQLite(db_name='test.db', entity=DebitCard))
  transaction_repository = TransactionsRepository(db=SQLite(db_name='test.db', entity=Transactions))
  
  transaction = DebitTransactionsUseCase(
    account_repository=accout_repository,
    debit_card_repository=debit_card_repository,
    transaction_repository=transaction_repository
  )
  
  print(transaction.get_transactions())