from app.models import User, Appointment

def test_user_model(test_database):
    user = User(username='test_user', type='client')
    test_database.session.add(user)
    test_database.session.commit()

    assert user.id is not None
    assert user.username == 'test_user'
