from unittest.mock import Mock
import pytest

from src.infra.services import hash_service
from ..register_user import RegisterUser
from src.domain.tests import mock_user
from faker import Faker
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.services.interface import HashPasswordService

faker = Faker()

pytestmark = pytest.mark.unit

def test_register_user():
    """ test register user success """

    user = mock_user()
    repository = Mock(spec=UserRepositoryInterface)
    hash_service = Mock(spec=HashPasswordService)
    use_case = RegisterUser(repository,hash_service)
    repository.select_user.return_value = []
    repository.insert_user.return_value = user
    hash_service.generate_password_hash.return_value = ""
    
    new_user = use_case.register(name=user.name,password=user.password, email=user.email, phone=str(user.phone), date_of_birth=str(user.date_of_birth))

    #test output
    assert new_user["success"] is True
    assert new_user["data"] == user


def test_register_user_fail():
    """ test register user fail """

    repository = Mock(spec=UserRepositoryInterface)
    hash_service = Mock(spec=HashPasswordService)
    use_case = RegisterUser(user_repository=repository, hash_service=hash_service)
    repository.select_user.return_value = [1]
    hash_service.generate_password_hash.return_value = ""


    user = mock_user()
    password = faker.name()
    name = faker.random_number()

    with pytest.raises(Exception, match="user already registered"):
        use_case.register(name=name, password=password, email=user.email, phone=user.phone, date_of_birth=user.date_of_birth)


    # #output
    # assert new_user["success"] is False
    # assert new_user["data"] is None


    