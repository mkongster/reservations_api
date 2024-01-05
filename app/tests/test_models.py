from app.models import User
from app.database import db

def test_user_model():
    user = User(username='test_user')
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert user.username == 'test_user'
