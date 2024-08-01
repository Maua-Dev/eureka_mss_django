from app.controllers.user.get_all_professors_controller import GetAllProfessorsController
from app.controllers.user.get_all_students_controller import GetAllStudentsController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

delivery_repo = Environments.get_delivery_repo()()
task_repo = Environments.get_task_repo()()
project_repo = Environments.get_project_repo()()
user_repo = Environments.get_user_repo()()

class UserViews:

    @staticmethod
    def get_all_students(request):
        controller = GetAllStudentsController(
            repo=user_repo
        )
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

    @staticmethod
    def get_all_professors(request):
        controller = GetAllProfessorsController(
            repo=user_repo
        )
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()