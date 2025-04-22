# tests/test_routes.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

import pytest

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask Web App' in response.data

def test_users_page(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b'User List' in response.data
