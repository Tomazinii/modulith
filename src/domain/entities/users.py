class Users:
    """ Entitie User model """

    def __init__(self, id, name, password, email, date_of_birth, phone):
        self.id = id
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.password = password

    def delete_account(self, id, password):
        """ if password == password -> remove account"""

        if password == self.password and id == self.id:
            is_remove = True
            return is_remove

        raise Exception("You need to pass your password and id")