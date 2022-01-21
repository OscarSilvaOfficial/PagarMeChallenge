from fastapi.testclient import TestClient
from api.infra.entrypoint import app
from fast_nosql_manager.implementations.mongo import MongoRepository

client = TestClient(app)
mongo = MongoRepository(db_name='pagarme', db_str_connection='mongodb://localhost:27017/')

def test_index():
  assert client.get('/').json() == {'message': 'Hello World'}
 
def test_get_accounts():
  assert client.get('/accounts').status_code == 200
  
def test_create_account():
  account = {
    "document": "12345678910",
    "user_name": "teste",
    "balance": 1000.0
  }
  
  try:
    mongo.delete_document(collection_name='accounts', where={'document': account['document']})
  except Exception as e:
    pass

  request = client.post('/accounts/', json=account)
  assert request.status_code == 201
  
def test_create_account_already_exists():
  account = {
    "document": "12345678904",
    "user_name": "teste",
    "balance": 1000.0
  }
  request = client.post('/accounts/', json=account)
  assert request.status_code == 409
  
def test_update_account():
  account = {
    "user_name": "SEI LA"
  }
  request = client.patch('/accounts/12345678904/', json=account)
  assert request.status_code == 204