from src.domain.use_case_interface.user import EditUser as EditUserInterface
from src.infra.interface.repo_interface import UserRepositoryInterface
from typing import Type, Dict
from src.domain.entities import Users

class EditUser(EditUserInterface):
    """ edit user use case: edit data user and change password method"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository
        
    
    def edit_user(self, id: int, name: str = None, email: str = None, phone: str = None, date_of_birth: str = None) -> Dict[bool, Users]:
        data = {}
        response = None

        if name != None and isinstance(name, str):
            data["name"] = name

        if email != None and isinstance(email, str):
            data["email"] = email

        if phone != None and isinstance(phone, str):
            data["phone"] = phone

        if date_of_birth != None and isinstance(date_of_birth, str):
            data["date_of_birth"] = date_of_birth
        
        if data.keys().__len__() != 0:
            response = self.user_repository.update_user(id=id, data=data)

            return {"success":True, "data": response}

        return {"success":False, "data": response}


    def change_password(self, id: int, new_password: str, re_password: str) -> str:
        return super().change_password(id, new_password, re_password)