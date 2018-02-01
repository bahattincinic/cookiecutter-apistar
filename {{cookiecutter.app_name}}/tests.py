import pytest

from apistar import TestClient, reverse_url

from app import app


@pytest.fixture
def setup_tables(scope="function"):
    app.main(['create_tables'])
    yield
    app.main(['drop_tables'])


def test_create(setup_tables):
    client = TestClient(app)
    response = client.post('/example', json={'name': 'Test'})
    assert response.status_code == 200
    assert response.json() == {"name": 'Test'}


def test_list(setup_tables):
    client = TestClient(app)
    client.post('/example', json={'name': 'Test'})
    response = client.get('/example')
    assert response.status_code == 200
