from ..register_user import RegisterUser
from src.infra.repo.faker import FakerUserRepository
from src.domain.tests import mock_user
from faker import Faker

faker = Faker()


def test_register_user():
    
    repository = FakerUserRepository()
    use_case = RegisterUser(repository)
    user = mock_user()
    new_user = use_case.register(name=user.name,password=user.password, email=user.email, phone=user.phone, date_of_birth=user.date_of_birth)

    #test inputs
    assert repository.db["name"] == user.name
    assert repository.db["email"] == user.email
    assert repository.db["password"] == user.password
    assert repository.db["phone"] == user.phone
    assert repository.db["date_of_birth"] == user.date_of_birth

    #test output
    assert new_user["success"] is True
    assert new_user["data"]


def test_register_user_fail():
    """ test register user fail """

    repository = FakerUserRepository()

    use_case = RegisterUser(user_repository=repository)

    user = mock_user()
    password = faker.name()
    name = faker.random_number()

    new_user = use_case.register(name=name, password=password, email=user.email, phone=user.phone, date_of_birth=user.date_of_birth)

    #input test
    assert repository.db == {}

    #output
    assert new_user["success"] is False
    assert new_user["data"] is None


    