from abc import ABC,abstractmethod
from typing import Dict
from src.domain.entities import Users
class UseCaseUser(ABC):


    @abstractmethod
    def register(self,name: str, password: str, id: int, email: str, phone: str) -> Dict[bool,Users]:
        """ interface to RegisterUser use case """

    @abstractmethod
    def get_user(self,name):
        """"""
        