from fastapi.testclient import TestClient
from api.infra.entrypoint import app


client = TestClient(app)

def test_create_transaction():
  transaction = {
    'from_document': "12345678904",
    'to_document': "12345678903",
    'value': 100.0
  }

  request = client.post('/transactions/', json=transaction)
  assert request.status_code == 201