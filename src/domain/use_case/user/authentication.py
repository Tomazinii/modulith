from src.domain.use_case_interface.user import AuthenticationUserInterface
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.services.interface import HashPasswordService,JwtServiceInterface
from src.domain.entities import Users
from src.domain.use_case.exceptions import UserNotFoundException,InvalidCredentialsException

from typing import Type, Dict

class Authentication(AuthenticationUserInterface):
    """ authentication login/logout """

    def __init__(self, repository: Type[UserRepositoryInterface],  hash_service: Type[HashPasswordService] , jwt_service: Type[JwtServiceInterface]):
        self.repository = repository
        self.hash_service = hash_service
        self.jwt_service = jwt_service

    def login(self, email: str, password: str) -> Dict[str, str]:
        user: Users = self.repository.select_user(email=email)

        if not user:
            raise UserNotFoundException()
        

        if self.hash_service.verify_password(password=password, pwd=user[0].password): # isso vai dar erro pq o user é uma lista
            user[0].is_authenticate = True # nao faz muito sendo se isso nao mudar dentro do banco de dados
            token = self.jwt_service.create_token(user=user[0])
            
            return token
        
        else:
            raise InvalidCredentialsException()



    def logout(self):
        return super().logout()

