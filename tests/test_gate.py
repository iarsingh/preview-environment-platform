from fastapi.testclient import TestClient
from preview.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'pr': 12, 'branch': 'feat/probes'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'pr': 12, 'branch': 'main'}).json()
    assert bad["passed"] is False
    assert "protected_branch" in bad["failed"]
