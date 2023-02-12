from .register_user import RegisterUser
from src.infra.repo.faker import FakerUserRepository
from src.domain.tests import mock_user

def test_register_user():
    repository = FakerUserRepository()

    use_case = RegisterUser(repository)

    user = mock_user()

    new_user = use_case.register(name=user.name, password=user.password, email=user.email, phone=user.phone, date_of_birth=user.date_of_birth)

    assert new_user["data"].name == repository.db[new_user["data"].name].name
    assert new_user["success"] == True

    