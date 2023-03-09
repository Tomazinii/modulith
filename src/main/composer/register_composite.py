from src.presenters.controllers.user_controller import RegisterUserController
from src.domain.use_case.user import RegisterUser
from src.infra.repo.user_repository import UserRepository
from src.infra.services import HashPassword


def register_composite():
    user_repository = UserRepository()
    hash_service = HashPassword()
    register_use_case = RegisterUser(user_repository,hash_service=hash_service)
    controller = RegisterUserController(register_usecase=register_use_case)
    return controller