
from src.infra.repo.user_repository import UserRepository
from src.infra.config.db_config import DBConnectionHandler
import pytest
from faker import Faker
from psycopg2.extras import DictCursor
faker = Faker()

pytestmark = pytest.mark.unit




class TestUserRepository:
    repo = UserRepository()
    db = DBConnectionHandler()
    conn = db.get_db()
    cur = conn.cursor(cursor_factory=DictCursor)


    def test_insert_user(self):

        user = self.repo.insert_user(name="alecrin",password="123",phone=faker.name(),date_of_birth="20/20/20",email=faker.email())
        self.cur.execute(f"SELECT * FROM users WHERE id={user.id};")
        query = self.cur.fetchone()
        self.cur.execute(f"DELETE FROM users WHERE id={user.id}")
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
        assert user.id == query["id"]
        assert user.name == query["name"]