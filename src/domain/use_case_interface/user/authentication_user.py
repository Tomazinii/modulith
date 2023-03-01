from abc import ABC, abstractmethod
from typing import Dict

class AuthenticationUserInterface(ABC):
    """ login interface method """

    @abstractmethod
    def login(self, email, password) -> Dict[str, str]:
        raise Exception("not implemented")

    @abstractmethod
    def logout(self):
        raise Exception("not implemented")
    
    
