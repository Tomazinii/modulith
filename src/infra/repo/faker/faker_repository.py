
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.entities import Users
from faker import Faker
from typing import Dict, List
from src.domain.tests import mock_user
from src.domain.services.interface import HashPasswordService
from typing import Type

faker = Faker()

class FakerUserRepository(UserRepositoryInterface):

    def __init__(self): #hash_service: Type[HashPasswordService]
        self.db = {}
    
    def insert_user(self, name: str, email: str, password: str, phone: str, date_of_birth ) -> Users:
        
        hash = self.hash_service.generate_password_hash(password="alecrindocampo")


        self.db["name"] = name
        self.db["email"] = email
        self.db["password"] = hash
        self.db["phone"] = phone
        self.db["date_of_birth"] = date_of_birth

        return mock_user()


    def select_user(self, email: str = None, user_id: int = None) -> List[Users]:

        self.db["email"] = email

        return [mock_user]


    def update_user(self, id: int, data: Dict) -> Users:
        return True

        