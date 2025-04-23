import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_welcome_route(client):
    """Test the welcome route returns the correct message."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to my Python build demo" in response.data
    assert response.mimetype == "text/html"


def test_welcome_route_content_type(client):
    """Test the welcome route returns HTML content type."""
    response = client.get("/")
    assert response.content_type == "text/html; charset=utf-8"
