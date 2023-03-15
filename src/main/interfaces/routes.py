from abc import ABC, abstractmethod
from src.presenters.helpers import HttpResponse, HttpRequest
from typing import Type


class RouteInterface(ABC):
    """ route interface use """

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception("method not implemented")