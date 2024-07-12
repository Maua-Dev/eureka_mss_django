from django.test import TestCase, RequestFactory

from app.controllers.project.create_project_controller import CreateProjectController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.project.project_repository_mock import ProjectRepositoryMock
from app.repos.user.user_repository_mock import UserRepositoryMock


class TestCreateProjectController(TestCase):

    def test_create_project_controller(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": len(project_repo.projects),
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "advisors": [4],
            "responsibles": [5],
            "students": [9]
        }
        
    def test_create_project_controller_without_students(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5],
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": len(project_repo.projects),
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "advisors": [4],
            "responsibles": [5],
            "students": []
        }
        
    def test_create_project_controller_without_responsibles(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": len(project_repo.projects),
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "advisors": [4],
            "responsibles": [],
            "students": [9]
        }
    
    def test_create_project_controller_without_advisors(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [],
                "responsibles": [5],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 201
        assert response.body == {
            "project_id": len(project_repo.projects),
            "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
            "qualification": "Engenharia de Software",
            "code": "ES-01",
            "shift": "DIURNO",
            "stand_number": "1",
            "is_entrepreneurship": False,
            "advisors": [],
            "responsibles": [5],
            "students": [9]
        }
        
    def test_create_project_controller_student_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "students": [len(user_repo.users)+1]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Estudante não encontrado"
        
    def test_create_project_controller_advisor_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [len(user_repo.users)+1],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Orientador não encontrado"
        
    def test_create_project_controller_responsible_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "responsibles": [len(user_repo.users)+1],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Responsável não encontrado"
        
    def test_create_project_controller_student_in_two_projects(self):
        user_repo = UserRepositoryMock()

        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "students": [len(user_repo.users), 1]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.message == "Estudante já cadastrado em um projeto"
        assert response.status_code == 403
        
    def test_create_project_controller_students_not_list(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "students": (1,2,3)
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Tipo de parâmetro incorreto para students"
        
    def test_create_project_controller_advisors_not_list(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": (4),
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Tipo de parâmetro incorreto para advisors"
        
    def test_create_project_controller_responsibles_not_list(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": (5)
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)
        
    def test_create_project_controller_user_id_is_missing(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field user_id is missing for method create_project"

    def test_create_project_controller_missing_title(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": None,
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 400
        assert response.message == "Field title is missing for method create_project"

    def test_create_project_controller_student_cannot_be_advisor(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [9],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não pode ser Orientador"

    def test_create_project_controller_student_cannot_be_responsible(self):
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "responsibles": [9],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não pode ser Responsável"

    def test_create_project_controller_user_id_not_found(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": len(user_repo.users)+2,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Usuário não encontrado"
        
    def test_create_project_controller_user_cannot_execute_route(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 1,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
        
    def test_create_project_controller_professor_cannot_execute_route(self):
        user_repo = UserRepositoryMock()
        request = DjangoHttpRequest(
            request=None,
            data={
                "user_id": 5,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "advisors": [4],
                "responsibles": [5],
                "students": [9]
            },
            method="POST"    
        )

        project_repo = ProjectRepositoryMock()
        controller = CreateProjectController(project_repo=project_repo, user_repo=user_repo)
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Professor não tem permissão para realizar esta ação"