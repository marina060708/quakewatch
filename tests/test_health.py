import importlib
from app import app  # top-level import is fine here

def test_app_imports():
    mod = importlib.import_module("app")
    assert hasattr(mod, "app")

def test_health_route():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
