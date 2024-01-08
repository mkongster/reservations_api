import pytest
from app import app, db
from app.models import Appointment, User, UserType
from datetime import datetime

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
        database_objects = [
            User(id=1, username='provider_user', type=UserType.provider),
            User(id=2, username='client_user', type=UserType.client),
            Appointment(id=1, provider_id=1, confirmed = False, slot_datetime = datetime(2025, 2, 1)),
            Appointment(id=2, provider_id=1, confirmed = False, slot_datetime = datetime(2024, 1, 1, 1)),
        ]
    
        db.session.add_all(database_objects)
        db.session.commit()
        yield db

    # Clean up the database after the test
    with app.app_context():
        db.session.remove()
        db.drop_all()