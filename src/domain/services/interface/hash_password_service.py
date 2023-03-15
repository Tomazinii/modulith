from abc import ABC, abstractmethod


class HashPasswordService(ABC):
    """ method hash password user authentication """

    @abstractmethod
    def generate_password_hash(password: bytes) -> str:
        raise Exception("method not implemented")

    @abstractmethod
    def verify_password(password: bytes, pwd:bytes ) -> bool:
        raise Exception("method not implemented")
