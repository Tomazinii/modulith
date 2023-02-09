from src.domain.entities import Users
from faker import Faker


faker = Faker()


def mock_user() -> Users:
    """mocking users"""

    user = Users(
        id = faker.random_number(),
        name = faker.name(),
        email = faker.email(),
        password = faker.name(),
        date_of_birth = faker.date(),
        phone = faker.phone_number()
    )

    return user