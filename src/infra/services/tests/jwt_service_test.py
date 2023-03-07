from cgitb import reset
import datetime
from time import sleep

import jwt
from src.infra.services import JwtService
import pytest
import secrets
from src.domain.tests import mock_user
import settings
from unittest.mock import Mock

from src.domain.entities import Users

pytestmark = pytest.mark.unit


class TestJwtService:

    def test_create_jwt(self):
        user = Users(2,"alecrin",email="a@a.com",date_of_birth="2-2-1000",phone="12345",password="qwerf")
        user.password = b"password"
        service = JwtService()
        result = service.create_token(user=user)
        assert result["access"]
        assert result["refresh"]
        assert isinstance(result, dict)

    def test_refresh_success(self):
        #data
        key = secrets.token_hex(10)
        user = mock_user()
        refresh_token = jwt.encode(vars(user),key=key, algorithm="HS256")
        service = JwtService()
        token = service.refresh_token(refresh_token=refresh_token, key=key)
        decoded_token = jwt.decode(token,key=key,algorithms=["HS256"])
        assert isinstance(token, str)
        assert decoded_token["name"] == user.name


    def test_refresh_fail(self):
        #data
        key = secrets.token_hex(10)
        user = mock_user()
        payload = vars(user)
        payload["exp"] = datetime.datetime.utcnow()
        refresh_token = jwt.encode(payload=payload,key=key,algorithm="HS256")
        service = JwtService()

        with pytest.raises(Exception, match="token invalid or expired"):
            service.refresh_token(refresh_token=refresh_token, key=key)

    def test_verify_sucess(self):
        key = secrets.token_hex(10)
        user = mock_user()
        payload = vars(user)
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        token = jwt.encode(payload=payload,key=key,algorithm="HS256")
        service = JwtService()
        result = service.verify_token(token,key=key)
        assert result is True

    def test_verify_fail(self):
        key = secrets.token_hex(10)
        user = mock_user()
        payload = vars(user)
        payload["exp"] = datetime.datetime.utcnow() 
        token = jwt.encode(payload=payload,key=key,algorithm="HS256")
        service = JwtService()

        with pytest.raises(Exception, match="token invalid or expired"):
            service.verify_token(token,key=key)
            