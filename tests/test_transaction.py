from api.entities.transaction.transaction import Transactions
from api.infra.db.sqlite import SQLite
from api.useCases.debit_transaction import DebitTransactionsUseCase
from api.entities.account.account import Account
from api.entities.card.debit_card import DebitCard
from api.adapters.repository.account_repository import AccountRepository
from api.adapters.repository.debit_card_repository import DebitCardRepository
from api.adapters.repository.transaction_repository import TransactionsRepository
from api.entities.validators.document.document_validator import DocumentValidator
from api.entities.validators.card.debit_card_validator import DebitCardValidator

# def test_create_accout():
#   SQLite(db_name='test.db')._create_tables()
#   accout_repository = AccountRepository(db=SQLite(db_name='test.db', entity=Account))
  
#   account = Account(
#     balance=1000,
#     document='12345678901',
#     user_name='John Doe',
#     validator=DocumentValidator
#   )
  
#   accout_repository.create_account(account)

# def test_create_debit_card():
#   SQLite(db_name='test.db')._create_tables()
#   card_repository = DebitCardRepository(db=SQLite(db_name='test.db', entity=Account))
  
#   card = DebitCard(
#     client_name='John Doe',
#     cvv='123',
#     expire_date='12/20',
#     number='1234567890123456',
#     validator=DebitCardValidator
#   )
  
#   card_repository.create_card(card)
  

# def test_transaction():
#   SQLite(db_name='test.db')._create_tables()
#   accout_repository = AccountRepository(db=SQLite(db_name='test.db', entity=Account))
#   debit_card_repository = DebitCardRepository(db=SQLite(db_name='test.db', entity=DebitCard))
#   transaction_repository = TransactionsRepository(db=SQLite(db_name='test.db', entity=Transactions))
  
#   transaction = DebitTransactionsUseCase(
#     account_repository=accout_repository,
#     debit_card_repository=debit_card_repository,
#     transaction_repository=transaction_repository
#   )
  
#   transaction.create_transaction(
#     card_number='1234567890123456',
#     cvv='123',  
#     from_document='12345678901',
#     to_document='12345678901',
#     value=100
#   )
  
#   assert len(transaction.get_transactions()) > 0
  