from src.domain.use_case_interface.user import FindUserInterface
from src.infra.interface.repo_interface import UserRepositoryInterface
from typing import Type
from src.domain.entities import Users


class FindUser(FindUserInterface):
    """ Find user class """

    def __init__(self, repository: Type[UserRepositoryInterface]):
        self.repository = repository

    def by_email(self, email)-> Users:
        """ select user by email field """
        
        if isinstance(email, str):
            if self.repository.select_user(email=email):
                user = self.repository.select_user(email=email)
                return user
            return Exception("User not found")
        
        raise Exception("invalid type input")


    def by_id(self, user_id):
        """ select user by id field """
        
        if isinstance(user_id, int):
            if self.repository.select_user(user_id=user_id):
                user = self.repository.select_user(user_id=user_id)
                return user
            raise Exception("User not found")
        
        raise Exception("invalid type input")



    