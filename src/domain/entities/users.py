class Users:
    """ Entitie User model """

    def __init__(self, id, name, email, date_of_birth, phone):
        self.id = id
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.__password = None

    def delete_account(self, id, password):
        """ if password == password -> remove account"""

        if password == self.__password and id == self.id:
            is_remove = True
            return is_remove

        raise Exception("You need to pass your password and id")


    def __repr__(self) -> str:
        return f"User(name:{self.name}, id:{self.id})"

    def get_password(self, user_id):
        if self.id == user_id:
            return self.__password

    def set_password(self, password):
        
        encrypt = True
        
        if encrypt:
            self.__password = password