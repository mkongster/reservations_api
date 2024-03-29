# test_my_module.py
import pytest
from app import reservations_system
from datetime import datetime
from freezegun import freeze_time


# Fixture to freeze time for the entire module
@pytest.fixture(autouse=True)
def frozen_time_module():
    frozen_datetime = datetime(2024, 1, 1)
    with freeze_time(frozen_datetime) as frozen:
        yield frozen


# Use the fixtures in your tests
def test_submit_availability(test_database):
    test_provider_id = 7
    test_appointments = [
        datetime(2024, 2, 1, 4, 20),
        datetime(2024, 2, 1, 9, 45),
        datetime(2024, 2, 1, 7, 30)
    ]
    appts = reservations_system.submit_availability(test_provider_id, test_appointments)
    assert len(appts) == 2


def test_reserve(test_database):
    client_id = 2
    appointment_id = 1
    appt = reservations_system.reserve(client_id=client_id, appointment_id=appointment_id)
    assert appt.last_reserved_by == client_id


def test_reserve_fail_within_24_hours(test_database):
    client_id = 2
    appointment_id = 2
    appt = reservations_system.reserve(client_id=client_id, appointment_id=appointment_id)
    assert appt == None


def test_reserve_fail_reserved_already(test_database):
    client_id = 2
    appointment_id = 3
    appt = reservations_system.reserve(client_id=client_id, appointment_id=appointment_id)
    assert appt == None


def test_confirm(test_database):
    client_id = 2
    appointment_id = 4
    appt = reservations_system.confirm(client_id=client_id, appointment_id=appointment_id)
    assert appt.client_id == client_id
    assert appt.confirmed == True


def test_get_available_appointments(test_database):
    appointments = reservations_system.get_available_appointments()
    assert len(appointments) == 4
