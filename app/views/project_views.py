from app.controllers.project.create_project_controller import CreateProjectController
from app.controllers.project.get_project_controller import GetProjectController
from app.controllers.project.get_projects_by_role_controller import GetProjectsByRoleController
from app.controllers.project.update_project_controller import UpdateProjectController
from app.environments import Environments
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.helpers.http.django_http_response import DjangoHttpResponse

project_repo = Environments.get_project_repo()()
user_repo = Environments.get_user_repo()()


class ProjectViews:
    @staticmethod
    def create_project(request):
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

    @staticmethod
    def update_project(request):
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()

    @staticmethod
    def get_project(request):
        controller = GetProjectController(project_repo)
        http_request = DjangoHttpRequest(request)
        response = controller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)

        return http_response.to_django()
    
    @staticmethod
    def get_projects_by_role(request):
        controlller = GetProjectsByRoleController(project_repo, user_repo)
        http_request = DjangoHttpRequest(request)
        response = controlller(http_request)
        http_response = DjangoHttpResponse(body=response.body, status_code=response.status_code,
                                           message=response.message)
        return http_response.to_django()
