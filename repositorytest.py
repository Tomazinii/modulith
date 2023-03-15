from src.infra.repo.user_repository import UserRepository
import psycopg2
from src.infra.entities import Users

from src.domain.entities.users import Users as UserEntitie
from src.infra.services import HashPassword
user_repo = UserRepository()

password_hash = HashPassword().generate_password_hash("123")

user_repo.insert_user(name="last",email="test@test.com", password=password_hash,date_of_birth="20234/20/15", phone="123132321")
