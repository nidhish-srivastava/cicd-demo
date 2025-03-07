import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# MESSAGE SHOULD be Hello world with 200 status code otherwise code will fail
def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data