# test_my_module.py
import pytest
from datetime import datetime
from app import reservations

# Define a fixture for common test data
@pytest.fixture
def input_data():
    return 2, 3

# Define a fixture for setup and teardown actions
@pytest.fixture
def setup_teardown_example():
    # Setup actions, if needed
    print("\nSetup actions before the test")

    # Yield control to the test function
    yield

    # Teardown actions, if needed
    print("\nTeardown actions after the test")

# Use the fixtures in your tests
def test_submit_availability(test_database):
    test_provider_id = 7
    test_appointments = [
        datetime(2024, 2, 1, 4, 20),
        datetime(2024, 2, 1, 9, 45),
        datetime(2024, 2, 1, 7, 30)
    ]
    appts = reservations.submit_availability(test_provider_id, test_appointments)
    assert len(appts) == 2

# Use the setup_teardown_example fixture
def test_example_with_setup_and_teardown(setup_teardown_example):
    assert True

# You can also use fixtures in a more modular way
@pytest.fixture
def setup_example():
    print("\nSetup actions before the test")
    yield
    print("\nTeardown actions after the test")

def test_modular_setup_example(setup_example):
    assert True
