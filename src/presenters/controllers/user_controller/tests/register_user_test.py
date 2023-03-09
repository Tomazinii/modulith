# from ..register_user import RegisterUserController
# from src.infra.repo.faker import FakerUserRepository
# from src.domain.use_case.user import RegisterUser
# from faker import Faker
# from src.presenters.helpers import HttpRequest

# faker = Faker()



# def test_register_user_controller():
#     controller = RegisterUserController(register_usecase=RegisterUser(FakerUserRepository()))

#     attributes = {"email": str(faker.email()), "password": str(faker.name()), "name": str(faker.name()), "phone": str(faker.random_number()),"date_of_birth":faker.date()}

#     response = controller.route(http_request=HttpRequest(body=attributes))

#     # assert response.body.name == attributes["name"]



