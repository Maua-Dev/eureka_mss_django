from django.test import TestCase, RequestFactory

from app.controllers.project.update_project_controller import UpdateProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock
from app.repos.user.user_repository_mock import UserRepositoryMock


class TestUpdateProjectController(TestCase):

    def test_update_project_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "user_id": 10,
                "title": "Estudando Computação Quântica",
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body['title'] == 'Estudando Computação Quântica'
        
    def test_update_project_controller_update_advisors(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "advisors": [8],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body['advisors'] == [8]

    def test_update_project_controller_student_can_update_with_restrictions(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "project_id": 1,
                "title": "Estudando Computação Quântica",
                
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.body['title'] == "Estudando Computação Quântica"

    def test_update_project_controller_missing_project_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "None",
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field project_id is missing for method update_project"
        
    def test_update_project_controller_missing_user_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 2,
                "title": "None",
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field user_id is missing for method update_project"

    def test_update_project_controller_not_found_project_id(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1000,
                "title": "Estudando Computação Quântica",
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Projeto não encontrado"
        
    def test_update_project_controller_student_not_found(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "students": [1000],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Estudante não encontrado"
        
    def test_update_project_controller_advisor_not_found(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "advisors": [1000],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Orientador não encontrado"
        
    def test_update_project_controller_responsible_not_found(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "responsibles": [1000],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Responsável não encontrado"
        
    def test_update_project_controller_student_already_in_project(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 2,
                "students": [1],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante já cadastrado em um projeto"
    
    def test_update_project_controller_update_same_student(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "students": [1],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 200
        
    def test_update_project_controller_student_cannot_be_advisor(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "advisors": [1],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não pode ser Orientador"
    
    def test_update_project_controller_student_cannot_be_responsible(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "project_id": 1,
                "responsibles": [1],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não pode ser Responsável"

    def test_update_project_controller_only_admin_can_change_students_field(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "project_id": 1,
                "students": [1],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
        
    def test_update_project_controller_only_admin_can_change_advisors_field(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "project_id": 1,
                "advisors": [4],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
        
    def test_update_project_controller_only_admin_can_change_responsibles_field(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "project_id": 1,
                "responsibles": [4],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
        
    def test_update_project_controller_user_cannot_change_responsibles_field(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "project_id": 1,
                "responsibles": [4],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
        
    def test_update_project_controller_professor_cannot_change_responsibles_field(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 5,
                "project_id": 1,
                "responsibles": [4],
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Professor não tem permissão para realizar esta ação"
       
    def test_update_project_controller_user_id_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": len(user_repo.users)+2,
                "project_id": 1,
                "title": "Estudando Computação Quântica",
            },
            method="PUT"
        )

        project_repo = ProjectRepositoryMock()
        controller = UpdateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Usuário não encontrado"