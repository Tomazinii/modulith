import http
from tkinter.messagebox import NO
from turtle import ht
from src.presenters.helpers import HttpRequest, HttpResponse
from typing import Type
from src.domain.use_case_interface.user import AuthenticationUserInterface
from src.presenters.errors import HttpErrors, http_error
from src.main.interfaces.routes import RouteInterface

class LoginController(RouteInterface): 

    def __init__(self,authentication_use_case: Type[AuthenticationUserInterface]):
        self.authentication_use_case = authentication_use_case


    def route(self, request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if request.body:
            params = request.body.keys()

            if "email" in params and "password" in params:
                email = request.body["email"]
                password = request.body["password"]
                response = self.authentication_use_case.login(
                    email=email, password=password
                )
            
            else:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"],body=http_error["body"]
                )

            return HttpResponse( status_code=200, body=response)
        
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code= http_error["status_code"],
            body=http_error["body"]
        )
