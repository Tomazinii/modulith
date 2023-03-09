from abc import ABC, abstractmethod
from src.domain.entities import Users

class FindUserInterface(ABC):

    @abstractmethod
    def by_id(self, user_id) -> Users:
        raise Exception("method not implemented")
    
    def by_email(self, email) -> Users:
        raise Exception("method not implemented")
    
    
    