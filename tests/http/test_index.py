from fastapi.testclient import TestClient
from api.infra.entrypoint import app


client = TestClient(app)

def test_index():
  assert client.get('/').json() == {'message': 'Hello World'}
 
def test_get_accounts():
  assert client.get('/accounts').status_code == 200
  
def test_create_account():
  accout = {
    "document": "12345678904",
    "user_name": "teste",
    "balance": 1000.0
  }
  request = client.post('/accounts/', json=accout)
  assert request.status_code == 201
  
def test_create_account_already_exists():
  accout = {
    "document": "12345678904",
    "user_name": "teste",
    "balance": 1000.0
  }
  request = client.post('/accounts/', json=accout)
  assert request.status_code == 409