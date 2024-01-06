import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

@pytest.fixture
def test_database():
    with app.app_context():
        db.create_all()
        yield db

    # Clean up the database after the test
    with app.app_context():
        db.session.remove()
        db.drop_all()