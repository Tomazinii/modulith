
from unittest.mock import Mock
import pytest
from src.domain.entities.users import Users
from src.domain.use_case.user import FindUser
from src.infra.interface.repo_interface.user_repositoy_interface import UserRepositoryInterface

pytestmark = pytest.mark.unit

class TestFindUser:

    def test_find_by_email(self):
        repo = Mock(spec=UserRepositoryInterface)
        value = repo.select_user.return_value = Users(1,"alecrin","a@a.com","00","1234","asdf")
        find = FindUser(repo)
        result = find.by_email("a@a.com")
        assert result == value

    def test_find_by_id(self):
        repo = Mock(spec=UserRepositoryInterface)
        value = repo.select_user.return_value = Users(1,"alecrin","a@a.com","00","1234","asdf")
        find = FindUser(repo)
        result = find.by_id(1)

        # assert result.id == value.id
        assert result.id == 2
        assert result.name == value.name
        