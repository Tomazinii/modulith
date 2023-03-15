from abc import ABC, abstractmethod
from src.domain.entities import Users
from typing import Type, Dict, List



class UserRepositoryInterface(ABC):
    """ repository interface """

    @abstractmethod
    def insert_user(self, name: str, email: str, password: str, phone:str, date_of_birth: str ) -> Users:
        raise Exception("method not implemented")

    @abstractmethod
    def select_user(self, email: str = None, user_id: int = None) -> List[Users]:
        raise Exception("method not implemented")

    @abstractmethod
    def update_user(self, id: int, data: Dict) -> Users:
        raise Exception("method not implemented")



