from src.domain.entities import Users
from .mock_user import mock_user
from faker import Faker

faker = Faker()

def test_remove_user():
    user_mock = mock_user()
    user_mock.set_password(faker.name())
    remove_status = user_mock.delete_account(user_mock.id,password=user_mock.get_password(user_mock.id))


    assert user_mock.get_password(user_mock.id) != None
    assert remove_status == True



    
