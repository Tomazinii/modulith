

class InvalidCredentialsException(Exception):
    
    def __init__(self, *args: object) -> None:
        self.message = "Email or password incorrect"
        super().__init__(self.message)