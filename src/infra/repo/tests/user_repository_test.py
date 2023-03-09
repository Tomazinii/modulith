
from src.infra.repo.user_repository import UserRepository
from src.infra.config.db_config import DBConnectionHandler
import pytest
from faker import Faker
from psycopg2.extras import DictCursor
from unittest.mock import Mock
from random import randint
from src.infra.entities import Users


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

    
    def test_select_user_email(self):
        #Arrange
        db_connection = DBConnectionHandler()
        user = Users(name=faker.name(), email=faker.email(), password=faker.name(), phone=faker.name(), date_of_birth="00-00-00")
        with db_connection:
            db_connection.session.add(user)
            db_connection.session.commit()

        #Act
            result = self.repo.select_user(user.email)

                    
        #Assert
        assert result[0].email == user.email
        assert result[0].id == user.id

        def delete_user():
            user_to_delete = db_connection.session.query(Users).filter_by(email=user.email).first()
            db_connection.session.delete(user_to_delete)
            db_connection.session.commit()
        delete_user()





 