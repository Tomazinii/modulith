import jwt
from ..authentication import Authentication
from src.infra.repo.faker import FakerUserRepository
import pytest
from faker import Faker
from src.infra.interface.repo_interface import UserRepositoryInterface

from src.domain.services.interface import HashPasswordService
from src.domain.entities import Users
from src.infra.services import HashPassword
from src.domain.services.interface import JwtServiceInterface
from src.infra.services import JwtService

from src.domain.tests import mock_user

from typing import Dict

faker = Faker()

pytestmark = pytest.mark.unit


from unittest.mock import Mock


class TestAuthentication:

    @pytest.fixture
    def hash_service(self):
        return Mock(spec=HashPasswordService)
    
    @pytest.fixture
    def jwt_service(self):
        return Mock(spec=JwtServiceInterface)
    
    @pytest.fixture
    def mock_user_repo(self):
        return Mock(spec=UserRepositoryInterface)
    
    def authenticate(self,repository, hash_service,jwt_service = JwtService):
        return Authentication(repository,hash_service,jwt_service)
    

    def test_login_user(self,hash_service,mock_user_repo):
        user_repository = mock_user_repo

        user_repository.select_user.return_value = Users(2,"alecrin",email="a@a.com",date_of_birth="2-2-1000",phone="12345",password="qwerf".encode())



        authentication = self.authenticate(repository=user_repository, hash_service=hash_service,jwt_service=JwtService)

        tokens = authentication.login(email=faker.email(),password=b"test")

        assert isinstance(tokens, dict)
        assert "access" in tokens 
        assert "refresh" in tokens 



    def test_user_not_found(self,hash_service,mock_user_repo):
        # Arrange
        email = "johndoe@example.com"
        password = "password"
        user_repository = mock_user_repo
        user_repository.select_user.return_value = []

        authentication = self.authenticate(repository=user_repository, hash_service=hash_service)
        

        # Act/Assert
        with pytest.raises(Exception, match="user not found"):
            authentication.login(email, password)

    
    def test_user_email_or_password_incorrect(self, hash_service, mock_user_repo):
        email = "johndoe@example.com"
        password = "password"

        hash_service.verify_password.return_value = False
        authentication = self.authenticate(repository=mock_user_repo, hash_service=hash_service)

        with pytest.raises(Exception, match="Email or password incorrect"):
            authentication.login(email, password)


        


