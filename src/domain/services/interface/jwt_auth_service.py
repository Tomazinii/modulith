from abc import ABC, abstractmethod

from src.domain.entities import Users
from typing import Dict


class JwtServiceInterface(ABC):

    @abstractmethod
    def create_token(self, user: Users, key: str, algorithm: str,life_time_access_token, life_time_refresh_token) -> Dict[str, str]:
        raise Exception("not implemented")
    
    @abstractmethod
    def refresh_token(self, refresh_token, key: str,algorithm: str, life_time_access_token) -> str:
        raise Exception("not implemented")

    @abstractmethod
    def verify_token(self):
        raise Exception("not implemented")
