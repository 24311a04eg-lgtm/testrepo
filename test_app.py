from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200

def test_get_tasks(client):
    res = client.get('/tasks')
    assert res.status_code == 200

def test_create_task(client):
    res = client.post('/tasks', json={"title": "Learn CI/CD"})
    assert res.status_code == 201

def test_complete_task(client):
    client.post('/tasks', json={"title": "Learn CI/CD"})
    res = client.put('/tasks/1')
    assert res.status_code == 200

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
