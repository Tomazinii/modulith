
import jwt
from src.presenters.controllers.user_controller import LoginController
from src.domain.use_case.user import Authentication
from src.infra.services import JwtService, HashPassword
from src.infra.repo.user_repository import UserRepository #put in the module init


#only test
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.entities import Users
from typing import List, Dict
from src.domain.tests.mock_user import mock_user
from src.infra.services import HashPassword


class RepositoryTest(UserRepositoryInterface):
    
    
    def __init__(self):
        password = HashPassword.generate_password_hash("123")

        self.db = {"a@a.com":Users(id=1,name="alecrin",email="a@a.com",date_of_birth="",password=password,phone="")}

    def insert_user(self, name: str, email: str, password: str, phone: str, date_of_birth: str) -> Users:
        return super().insert_user(name, email, password, phone, date_of_birth)
    
    def update_user(self, id: int, data: Dict) -> Users:
        return super().update_user(id, data)

    def select_user(self, email: str = None, user_id: int = None) -> List[Users]:

        try:
            if self.db[email]:
                user = self.db[email]

            return user
        except:
            Exception("user not found")



def login_user_compose():
    hash_service = HashPassword()
    jwt = JwtService()
    repository = RepositoryTest()
    use_case_authentication = Authentication(repository=repository, hash_service=hash_service, jwt_service=jwt)
    controller = LoginController(authentication_use_case=use_case_authentication)

    return controller