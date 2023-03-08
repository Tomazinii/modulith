from sqlalchemy import Column, Integer, String, Boolean

# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
from src.infra.config.db_base import Base


class Users(Base):
    """ Entitie User model """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    date_of_birth = Column(String, unique=False, nullable=False)
    phone = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_authenticate = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(name={self.name}, id={self.id}, email={self.email})"
    
    def __eq__(self, other: object) -> bool:
        if(
            self.id == other.id,
            self.email == other.email
        ):
            return True
        return False