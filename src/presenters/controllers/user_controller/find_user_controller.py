from flask import request
from src.main.interfaces.routes import RouteInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from typing import Type
from src.domain.use_case_interface.user import FindUserInterface
from src.presenters.errors import HttpErrors

class FindUserController(RouteInterface):

    def __init__(self, find_user_use_case: Type[FindUserInterface]):
        self.use_case = find_user_use_case
        

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None


        if http_request.query:

            query = http_request.query.keys()



            if "email" in query and "id" not in query:
                response = self.use_case.by_email(email=http_request.query["email"])[0] #provisorio


            elif "id" in query and "email" not in query:
                response = self.use_case.by_id(user_id=http_request.query["id"])[0]  #provisorio


            
            elif "id" in query and "email" in query:
                response = self.use_case.by_id(id)[0]  #provisorio

            else:
                http_erro = HttpErrors()
                return HttpResponse(status_code=http_erro.error_422()["status_code"], body="asdf") #corrigir
            
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI
            response = vars(response)
            del response["_sa_instance_state"]
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI
            #ISSO É UM SERIALIZER NAO DEVE ESTÁ AQUI

            return HttpResponse(200, response)
        
        http_erro = HttpErrors.error_400()
        return HttpResponse(400, http_erro["body"])