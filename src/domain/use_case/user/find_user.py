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
            user = self.repository.select_user(email=email)
            return user
        
        raise Exception("invalid type input")



    def by_id(self, user_id):
        """ select user by id field """
        
        if isinstance(user_id, int):
            user = self.repository.select_user(user_id=id)
            return user
        
        raise Exception("invalid type input")



    