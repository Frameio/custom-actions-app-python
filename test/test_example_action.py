from fastapi.testclient import TestClient

import pytest

from custom_actions import router


client = TestClient(router)

def test_example_action():
    response = client.post("/test_action")
    assert response.status_code == 200
    assert response.json() != ""