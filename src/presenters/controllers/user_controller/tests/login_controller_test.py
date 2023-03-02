import re
from src.presenters.controllers.user_controller import LoginController
from unittest.mock import Mock
import pytest
from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.use_case_interface.user import AuthenticationUserInterface
from src.presenters.helpers import HttpRequest
pytestmark = pytest.mark.unit

class TestLoginController:
    
    
    @pytest.fixture
    def authentication_use_case_mock(self):
        return Mock(spec=AuthenticationUserInterface)

    def login_controller(self,authentication_use_case):
        return LoginController(authentication_use_case)

    def test_route(self):
        http_request = Mock(spec=HttpRequest)
        http_request.body = {"email":"a@a.com","password":"123"}


        authentication_use_case = Mock(spec=AuthenticationUserInterface)
        body = authentication_use_case.login.return_value = {"access":"Token","refresh":"Token"}


        login_controller = LoginController(authentication_use_case=authentication_use_case)

        result = login_controller.route(request=http_request)

        assert result.status_code == 200
        assert result.body == body
