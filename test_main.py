from fastapi.testclient import TestClient
from fastapi import status
from main import app
import pytest


client=TestClient(app)

def test_status_healthy():
    response = client.get('/')
    assert response.status_code==200
    assert response.json() == {"health_check": "OK"}

def test_language_predict():
    request_data = { "text": "mi nombre es Sweve"}
    response = client.post('/predict', json=request_data)
    assert response.status_code == 200
    assert response.json() == "Spanish"