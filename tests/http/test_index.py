from fastapi.testclient import TestClient
from api.infra.entrypoint.run import app


client = TestClient(app)

def test_index():
  print(client.get('/'))