class Users:
    """ Entitie User model """

    def __init__(self, id, name, email, date_of_birth, phone, password):
        self.id = id
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.password = password
        self.is_authenticate = False
        self.is_active = True
        

    def delete_account(self, id, password):
        """ if password == password -> remove account"""

        if password == self.password and id == self.id:
            is_remove = True
            self.is_active = False
            return is_remove

        raise Exception("You need to pass your password and id")


    def __repr__(self) -> str:
        return f"User(name:{self.name}, id:{self.id})"


