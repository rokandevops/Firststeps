import sys
import os

sys.path.append(os.path.abspath("."))
from fastapi.testclient import TestClient
from src.app import app
client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "we have done it"}