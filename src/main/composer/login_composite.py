
import jwt
from src.presenters.controllers.user_controller import LoginController
from src.domain.use_case.user import Authentication
from src.infra.services import JwtService, HashPassword
from src.infra.repo import UserRepository #put in the module init


def login_user_compose():
    hash_service = HashPassword()
    jwt = JwtService()
    repository = UserRepository()
    use_case_authentication = Authentication(repository=repository, hash_service=hash_service, jwt_service=jwt)
    controller = LoginController(authentication_use_case=use_case_authentication)

    return controller