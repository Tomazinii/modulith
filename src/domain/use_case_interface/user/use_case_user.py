from abc import ABC,abstractmethod
from typing import Dict
from src.domain.entities import Users


class RegisterUser(ABC):

    @abstractmethod
    def register(self,name: str, password: str, email: str, phone: str) -> Dict[bool, Users]:
        """ interface to RegisterUser use case """
