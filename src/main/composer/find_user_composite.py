from src.infra.repo import UserRepository
from src.domain.use_case.user import FindUser
from src.presenters.controllers.user_controller import FindUserController


def find_user_composite():
    repository = UserRepository()
    use_case = FindUser(repository)
    controller = FindUserController(use_case)
    
    return controller