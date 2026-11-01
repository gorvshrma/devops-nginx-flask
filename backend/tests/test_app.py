
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_hello(client):
    response = client.get("/api/hello")

    assert response.status_code == 200
    assert response.json["service"] == "flask-backend"


def test_products(client):
    response = client.get("/api/products")

    assert response.status_code == 200
    assert len(response.json["products"]) == 3


def test_health(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_readiness(client):
    response = client.get("/readyz")

    assert response.status_code == 200
    assert response.json["status"] == "ready"

