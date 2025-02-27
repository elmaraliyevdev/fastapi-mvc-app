from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def setup_module():
    client.delete("/auth/delete_all_users")

def test_signup():
    response = client.post("/auth/signup", json={"email": "test2@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "email" in response.json()

def test_login():
    response = client.post("/auth/login", data={"username": "test2@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_add_post():
    login_resp = client.post("/auth/login", data={"username": "test2@example.com", "password": "testpassword"})
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/posts/add", json={"text": "Testing post"}, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()