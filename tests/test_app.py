""" test """

import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Create the database
        yield app
        db.drop_all()  # Drop the database after the test

@pytest.fixture
def client(app):
    return app.test_client()

def test_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b"User List" in response.data
