from src.infra.repo.user_repository import UserRepository
import psycopg2
from src.infra.entities import Users

from src.domain.entities.users import Users as UserEntitie

user_repo = UserRepository()
user_repo.insert_user(name="last",email="last@as.com", password="qq",date_of_birth="20234/20/15", phone="1234")
