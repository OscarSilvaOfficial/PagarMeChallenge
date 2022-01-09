from api.entities.account import Accout
from api.adapters.validators.document.document_validator import DocumentValidator

def test_valid_document():
  account = Accout(
    document='12345678901', 
    user_name='user', 
    balance=100.0,
    validator=DocumentValidator
  )
  assert account.document == '12345678901' and account.user_name == 'user' and account.balance == 100.0
  
def test_with_no_document():
  try:
    Accout(
      document=None, 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document is required'
    
def test_long_document():
  try:
    Accout(
      document='123456789011', 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document must have 11 characters'
    
def test_no_only_digits_document():
  try:
    Accout(
      document='1234567890a', 
      user_name='user', 
      balance=100.0,
      validator=DocumentValidator
    )
  except ValueError as error:
    assert error.args[0] == 'Document must have only numbers'