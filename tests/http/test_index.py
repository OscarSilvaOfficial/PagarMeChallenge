from fastapi.testclient import TestClient
from api.infra.entrypoint.run import app


client = TestClient(app)

def test_index():
  assert client.get('/').json() == {'message': 'Hello World'}