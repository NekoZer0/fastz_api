from sqlalchemy import select

from fastz_api.models import User


def test_create_user_model(session):
    new_user = User(
        username='testuser',
        email='testuser@example.com',
        password='testpassword',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(User).where(User.email == 'testuser@example.com')
    )

    assert new_user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert new_user.password == 'testpassword'
