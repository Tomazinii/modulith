from abc import ABC, abstractmethod
from src.domain.entities import Users

class UserRepositoryInterface(ABC):
    """ repository interface """

    @abstractmethod
    def insert_user(self, name: str, email: str, password: str, phone:str, date_of_birth: str ) -> Users:
        raise Exception("method not implemented")



