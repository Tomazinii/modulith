from src.domain.entities import Users
from .mock_user import mock_user


def test_remove_user():
    user_mock = mock_user()
    remove_status = user_mock.delete_account(user_mock.id,user_mock.password)

    assert remove_status == True



    
