from fastapi.testclient import TestClient
from api.infra.entrypoint.run import app


client = TestClient(app)

def test_index():
  assert client.get('/api').json() == {'message': 'Hello World'}
 
def test_get_accounts():
  assert client.get('/api/accounts').status_code == 200
  
def test_create_account():
  accout = {
    "document": "12345678904",
    "user_name": "teste",
    "balance": 1000.0
  }
  request = client.post('/api/accounts/', json=accout)
  assert request.status_code == 201