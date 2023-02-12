from src.domain.entities import Users
from faker import Faker
from .edit_user import EditUser

from src.infra.repo.faker import  FakerUserRepository

faker = Faker()

def test_edit_user():
    repository = FakerUserRepository()

    edit = EditUser(user_repository=repository)
    
    valid = edit.edit_user(id=faker.random_number(), name=faker.name(), email=faker.email(), phone=faker.phone_number(), date_of_birth=faker.date())

    invalid = edit.edit_user(id=faker.random_number(), name=faker.random_number())

    not_pass_data = edit.edit_user(id=faker.random_number())

    assert valid["success"] == True
    assert valid["data"] != None
    assert invalid["success"] == False
    assert invalid["data"] == None
    assert not_pass_data["data"] == None


