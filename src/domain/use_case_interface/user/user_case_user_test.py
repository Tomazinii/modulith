class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class UserRepository:
    def get_user(self, user_id):
        raise NotImplementedError

class FakeUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)


class GetUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        return self.user_repository.get_user(user_id)


def test_get_user_use_case():
    # Configura o repositório falso
    fake_repository = FakeUserRepository()
    fake_repository.add_user(User(1, "User 1", "user1@example.com"))

    # Injeta o repositório falso no caso de uso
    use_case = GetUserUseCase(fake_repository)

    # Executa o caso de uso
    user = use_case.execute(1)

    # Verifica o resultado
    assert user.name == "User 1"
    assert user.email == "user1@example.com"

