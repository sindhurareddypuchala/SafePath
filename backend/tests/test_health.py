from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_liveness_check():
    response = client.get("/health/liveness")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data

def test_readiness_check():
    response = client.get("/health/readiness")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ("ready", "degraded")
    assert "database" in data
    assert "status" in data["database"]
    assert "postgres" in data["database"]
    assert "postgis" in data["database"]
