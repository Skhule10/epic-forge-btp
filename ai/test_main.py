from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_success():
    response = client.get("/predict", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 200
    assert isinstance(response.(), dict)  # Assuming the response is a JSON object

def test_predict_authentication_error():
    response = client.get("/predict", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401

def test_predict_network_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Network failure")

    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get("/predict", headers={"Authorization": "Bearer testtoken"})
    assert response.status_code == 500
    assert "Network failure" in response.()["detail"]
