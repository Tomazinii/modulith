from src.infra.interface.repo_interface import UserRepositoryInterface
from src.domain.entities.users import Users
from typing import List, Dict
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UserModel
from sqlalchemy.orm.exc import NoResultFound

class UserRepository(UserRepositoryInterface):
    """ Connection db  """

    @classmethod
    def insert_user(cls, name: str, email: str, password: str, phone: str, date_of_birth: str) -> Users:

        try:
            with DBConnectionHandler() as db_connection:
                new_user = UserModel(name=name, email=email, password=password, date_of_birth=date_of_birth, phone=phone)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(new_user.id, new_user.name, new_user.email, new_user.date_of_birth, new_user.phone, new_user.password)

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    
    @classmethod
    def select_user(cls, email: str = None, user_id: int = None) -> List[Users]:

        try:
            query = None
            if email and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UserModel).filter_by(email=email).one()
                    query = [data]

            elif user_id and not email:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UserModel).filter_by(id=user_id).one()
                    query = [data]

            elif email and user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UserModel).filter_by(email=email,id=user_id).one()
                    query = [data]

            return query

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None

    
    @classmethod
    def update_user(self, id: int, data: Dict) -> Users:
        return super().update_user(id, data)