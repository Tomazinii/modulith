
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.infra.entities import Users


engine = create_engine("postgresql://postgres:123@localhost:5432/ecommerce")

Session = sessionmaker(bind=engine)
session = Session()

user = session.query(Users).filter_by(id=130).first()

user.name = "alecrin do campo"
session.commit()


print(user)


