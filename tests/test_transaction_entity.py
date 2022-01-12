from api.entities.account import Accout
from api.entities.transaction import Transaction
from api.entities.validators.document.document_validator import DocumentValidator
from api.entities.validators.card.debit_card_validator import DebitCardValidator
from api.entities.validators.card.credit_card_validator import CreditCardValidator
from api.entities.debit_card import DebitCard
from api.entities.credit_card import CreditCard


def test_transaction_with_debit_card():
  from_account = Accout('07267865941', 'Oscar da Silva', 1000, DocumentValidator)
  to_account = Accout('07267865942', 'Oscar da Silvio', 1000, DocumentValidator)
  
  card = DebitCard(
    client_name='Oscar da Silva',
    cvv='123',
    expire_date='29/12/2029',
    number='1234567890123456',
    validator=DebitCardValidator,
  )
  
  transaction = Transaction(description="Test transaction")
  transaction.create_debit_transaction(
    card=card,
    value=100,
    to_account=to_account,
    from_account=from_account
  )
  
  assert from_account.balance == 900 and to_account.balance == 1100
    
    
def test_transaction_with_credit_card():
  to_account = Accout('07267865942', 'Oscar da Silvio', 1000, DocumentValidator)
  
  card = CreditCard(
    client_name='Oscar da Silva',
    cvv='123',
    expire_date='29/12/2029',
    number='1234567890123456',
    validator=CreditCardValidator,
    credit_limit=1000,
  )
  
  transaction = Transaction(description="Test transaction")
  transaction.create_credit_transaction(
    card=card,
    value=100,
    to_account=to_account
  )
  
  assert card.credit_limit == 900 and to_account.balance == 1100
    