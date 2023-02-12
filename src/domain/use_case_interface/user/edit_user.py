from abc import ABC, abstractmethod
from src.domain.entities import Users
from typing import Dict

class EditUser(ABC):
    """ edit user use case """

    @abstractmethod
    def edit_user(self, id: int, name: str = None, email: str = None, phone: str = None, date_of_birth: str = None) -> Dict[bool, Users]:
        """ edit username """
        raise Exception("you need pass the name ")

    @abstractmethod
    def change_password(self, id: int, new_password: str , re_password: str) -> str:
        """ change password method """
        raise Exception("you need pass password ")