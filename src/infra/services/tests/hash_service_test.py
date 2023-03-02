from faker import Faker
from src.infra.services.hash_service import HashPassword
import pytest

faker = Faker()

pytestmark = pytest.mark.unit

def test_hash_password():
    password = faker.name() 
    hash = HashPassword.generate_password_hash(password=password)
    verify = HashPassword.verify_password(password=password, pwd=hash)
    assert hash
    assert verify is True