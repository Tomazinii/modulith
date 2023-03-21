import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.base import settings

conn = psycopg2.connect(
    host=settings.HOST,
    database=settings.DATABASE,
    user=settings.USER,
    password=settings.PASSWORD,
)


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = settings.DATABASE_URL
        self.session = None

    def get_db(self):
        return conn


    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker(bind=engine)
        self.session = session_maker()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() 

