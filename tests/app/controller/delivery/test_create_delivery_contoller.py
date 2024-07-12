from django.test import TestCase

from app.controllers.delivery.create_delivery_controller import CreateDeliveryController
from app.helpers.http.django_http_request import DjangoHttpRequest
from app.repos.delivery.delivery_repository_mock import DeliveryRepositoryMock
from app.repos.delivery.delivery_repository_postgres import DeliveryRepositoryPostgres
from app.repos.project.project_repository_mock import ProjectRepositoryMock
from app.repos.project.project_repository_postgres import ProjectRepositoryPostgres
from app.repos.task.task_repository_mock import TaskRepositoryMock
from app.repos.task.task_repository_postgres import TaskRepositoryPostgres
from app.repos.user.user_repository_mock import UserRepositoryMock


class Test_CreateDeliveryController(TestCase):

    def test_create_delivery_controller(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 201
        
    def test_create_delivery_controller_error_handling(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request1 = DjangoHttpRequest(
            request=None,
            data={
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response1 = controller(request1)
        assert response1.status_code == 400
        assert response1.message == "Field task_id is missing for method create_delivery"
        
        request2 = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response2 = controller(request2)
        assert response2.status_code == 400
        assert response2.message == "Field project_id is missing for method create_delivery"
        
        request3 = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response3 = controller(request3)
        assert response3.status_code == 400
        assert response3.message == "Field user_id is missing for method create_delivery"
        
        request4 = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "user_id": 1,
            },
            method="POST"
        )
        response4 = controller(request4)
        assert response4.status_code == 400
        assert response4.message == "Field content is missing for method create_delivery"
        
        request5 = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="GET"
        )
        response5 = controller(request5)
        assert response5.status_code == 404
        assert response5.message == "Requisição não encontrada"
        
    def test_create_delivery_controller_task_not_found(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 100,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Tarefa não encontrada"    
           
    def test_create_delivery_controller_project_not_found(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 100,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Projeto não encontrado"    
           
    def test_create_delivery_controller_user_not_found(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 1,
                "project_id": 1,
                "user_id": 100,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 404
        assert response.message == "Usuário não encontrado"  
             
    def test_create_delivery_controller_project_student_creating_advisors_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 2,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"    
           
    def test_create_delivery_controller_project_student_creating_responsible_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 3,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"  
             
    def test_create_delivery_controller_project_student_creating_admin_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 8,
                "project_id": 1,
                "user_id": 1,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"       
        
        
    def test_create_delivery_controller_project_advisor_creating_responsible_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 3,
                "project_id": 1,
                "user_id": 4,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Orientador não tem permissão para realizar esta ação"       

    def test_create_delivery_controller_project_advisor_creating_admin_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 8,
                "project_id": 1,
                "user_id": 4,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Orientador não tem permissão para realizar esta ação"

    def test_create_delivery_controller_project_responsible_creating_admin_task(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 8,
                "project_id": 1,
                "user_id": 5,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Responsável não tem permissão para realizar esta ação"

    def test_create_delivery_controller_student_not_in_project(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 3,
                "project_id": 1,
                "user_id": 6,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Estudante não tem permissão para realizar esta ação"
           
    def test_create_delivery_controller_advisor_not_in_project(self):
        delivery_repo = DeliveryRepositoryMock()
        project_repo = ProjectRepositoryMock()
        task_repo = TaskRepositoryMock()
        user_repo = UserRepositoryMock()
        controller = CreateDeliveryController(delivery_repo=delivery_repo, project_repo=project_repo, task_repo=task_repo, user_repo=user_repo)
        request = DjangoHttpRequest(
            request=None,
            data={
                "task_id": 3,
                "project_id": 1,
                "user_id": 7,
                "content": {
                    "key": "value"
                }
            },
            method="POST"
        )
        response = controller(request)

        assert response.status_code == 403
        assert response.message == "Professor não tem permissão para realizar esta ação"   
