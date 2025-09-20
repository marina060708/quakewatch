import importlib
import types

def test_app_imports():
    # Ensure app.py exists and defines 'app'
    mod = importlib.import_module("app")
    assert isinstance(getattr(mod, "app", None), types.ModuleType) is False
    assert hasattr(mod, "app")

def test_health_route(monkeypatch):
    # Lazy import to avoid issues if flask isn't installed in user env outside CI
    from app import app
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
