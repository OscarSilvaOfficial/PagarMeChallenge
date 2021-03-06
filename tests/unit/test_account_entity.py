from api.entities.account.account import Account
from api.entities.validators.document.document_validator import DocumentValidator

def test_valid_document():
  account = Account(
    document='12345678901', 
    user_name='user', 
    balance=100.0,
    validator=DocumentValidator
  )
  assert account.document == '12345678901' and account.user_name == 'user' and account.balance == 100.0
  
def test_with_no_document():
  try:
    Account(
      document=None, 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document is required'
    
def test_long_document():
  try:
    Account(
      document='123456789011', 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document must have 11 characters'
    
def test_no_only_digits_document():
  try:
    Account(
      document='1234567890a', 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document must have only numbers'