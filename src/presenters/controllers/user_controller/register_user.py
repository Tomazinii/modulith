from src.main.interfaces import RouteInterface
from src.presenters.helpers import HttpRequest,HttpResponse
from typing import Type
from src.domain.use_case_interface.user import RegisterUser
from src.presenters.errors import HttpErrors


class RegisterUserController(RouteInterface):
    """ register user controller """

    def __init__(self, register_usecase: Type[RegisterUser]):
        self.register_usecase = register_usecase

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        response = None

        if http_request.body:
            body_params = http_request.body.keys()

            if "email" in body_params and "name" in body_params and "password" in body_params and "phone" in body_params and "date_of_birth" in body_params:
                email = http_request.body["email"]
                phone = http_request.body["phone"]
                password = http_request.body["password"]
                name = http_request.body["name"]
                date_of_birth = http_request.body["date_of_birth"]
                response = self.register_usecase.register(email=email, password=password, phone=phone, name=name, date_of_birth=date_of_birth)
  
                response_data = vars(response["data"]) # isso nao deve ser feito aqui!
            else:
                http_error = HttpErrors.error_422()
                return HttpResponse(http_error["status_code"], http_error["body"])

            return HttpResponse(200, response_data)

        http_error = HttpErrors.error_400()

        return HttpResponse(http_error["status_code"], http_error["body"])
        
