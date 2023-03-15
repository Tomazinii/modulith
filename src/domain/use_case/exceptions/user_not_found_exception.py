

class UserNotFoundException(Exception):

    def __init__(self, *args: object) -> None:
        self.message = "User not found"
        super().__init__(self.message)