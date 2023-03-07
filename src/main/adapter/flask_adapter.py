from src.main.interfaces.routes import RouteInterface
from typing import Type
from src.presenters.helpers import HttpRequest,HttpResponse



def flask_adapter(request: any, api_route: Type[RouteInterface]):
    try:
        http_request = HttpRequest(body=request.json)
        response = api_route.route(http_request)
        return response
    except Exception as exc:
        return HttpResponse(400, body=str(exc))