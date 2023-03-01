from abc import ABC, abstractmethod

from src.domain.entities import Users
from typing import Dict


class JwtServiceInterface(ABC):

    @abstractmethod
    def create_token(self, user: Users) -> Dict[str,str]:
        raise Exception("not implemented")
    
    @abstractmethod
    def refresh_token(self) -> str:
        raise Exception("not implemented")

    @abstractmethod
    def verify_token(self):
        raise Exception("not implemented")
