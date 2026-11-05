from fastapi.testclient import TestClient
from app import app, add

client = TestClient(app)


def test_add():
    assert add(2, 3) == 5


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
