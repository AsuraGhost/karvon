import pytest
from fastapi.testclient import TestClient

from karvon.config import Settings
from karvon.main import create_app


@pytest.fixture
def client(tmp_path):
    settings = Settings(database_url=f"sqlite:///{tmp_path / 'test.db'}", seed_demo=False)
    with TestClient(create_app(settings)) as c:
        yield c


@pytest.fixture
def demo_client(tmp_path):
    settings = Settings(database_url=f"sqlite:///{tmp_path / 'demo.db'}", seed_demo=True)
    with TestClient(create_app(settings)) as c:
        yield c


def gate_in(client, plate="01A123BC", passport="AA0000001", **extra):
    body = {"plate_number": plate, "driver_name": "Test Driver", "driver_passport": passport}
    r = client.post("/api/v1/visits", json=body | extra)
    assert r.status_code == 201, r.text
    return r.json()
