
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.entities import Users
from faker import Faker

faker = Faker()

class FakerUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.db = {}
    
    def insert_user(self, name: str, email: str, password: str, phone: str, date_of_birth ) -> Users:

        new_user = Users(name=name, email=email, password=password, phone=phone, id=5,date_of_birth=date_of_birth)

        try:
            self.db[new_user.name] = new_user

            return new_user
        except:
            raise Exception("Error")

        return None

        