from src.main.interfaces.routes import RouteInterface
from typing import Type
from src.presenters.helpers import HttpRequest,HttpResponse
from src.presenters.errors import HttpErrors

http_error = HttpErrors()

def flask_adapter(request: any, api_route: Type[RouteInterface]):

    try:
        query_string = request.args.to_dict()

        if "email" in query_string.keys():
            query_string["email"] = str(query_string["email"])
        if "id" in query_string.keys():
            query_string["id"] = int(query_string["id"])

    except:
        return HttpResponse(status_code=400,body=http_error.error_400()["body"])
    

    http_request = HttpRequest(header=request.headers,body=request.json, query=query_string)
        
    try:
        response = api_route.route(http_request)

        return response
    except Exception as exc:
        return HttpResponse(400, body=str(exc))