from src.domain.use_case_interface.user import RegisterUser as RegisterUserInterface
from typing import Dict, Type
from src.domain.entities import Users
from src.infra.interface.repo_interface import UserRepositoryInterface


class RegisterUser(RegisterUserInterface):
    """ use case Register user """

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository


    def verify_if_user_is_register_email(self,email) -> bool:
        
        user_email = self.user_repository.select_user(email=email)

        if user_email.__len__() == 0:
            return True
        return False


    def register(self, name: str, password: str, email: str, phone: str, date_of_birth: str) -> Dict[bool, Users]:
        """ validate datas and register user method """

        response = None
        
        validate_type = isinstance(name,str) and isinstance(password,str) and isinstance(email, str) and isinstance(phone, str)
  
        verify_user = self.verify_if_user_is_register_email(email=email)

        if validate_type and verify_user:
            response = self.user_repository.insert_user(name=name, password=password, email=email,phone=phone,date_of_birth=date_of_birth)
            return {"success": validate_type, "data": response}
        return {"success": False, "data": response}


