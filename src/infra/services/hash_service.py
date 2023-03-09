import bcrypt
from src.domain.services.interface import HashPasswordService


class HashPassword(HashPasswordService):
    """ hash passoword method """

    @staticmethod
    def generate_password_hash(password: bytes) -> str:

        if type(password) is not bytes:
            password = HashPassword.validate_encode(password)

        gen = bcrypt.gensalt()
        hash = bcrypt.hashpw(password=password, salt=gen)
        
        return hash
        

    @staticmethod
    def verify_password(password: bytes, pwd: bytes) -> bool:
        if type(password) is not bytes:
            password = HashPassword.validate_encode(password)

        if type(pwd) is not bytes:
            pwd = HashPassword.validate_encode(pwd)

        if bcrypt.checkpw(password=password, hashed_password=pwd):
            return True
        
        return False

    def validate_encode(password):
        password = password.encode()

        return password


