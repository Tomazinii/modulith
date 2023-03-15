import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


conn = psycopg2.connect(
    host="dbpostgres",
    database="ecommerce",
    user="postgres",
    password="123"
)


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "postgresql://postgres:123@dbpostgres:5432/ecommerce"
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

