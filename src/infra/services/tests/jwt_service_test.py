from src.infra.services import JwtService
import pytest
import secrets

from src.domain.tests import mock_user

pytestmark = pytest.mark.unit


class TestJwtService:

    def test_create_jwt(self):
        user = mock_user()

        service = JwtService()

        result = service.create_token(user=user)
        
        assert result["access"]
        assert result["refresh"]
        assert isinstance(result, dict)
        