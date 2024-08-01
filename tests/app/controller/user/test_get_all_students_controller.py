from django.test import TestCase, RequestFactory

from app.controllers.user.get_all_students_controller import GetAllStudentsController
from app.repos.user.user_repository_mock import UserRepositoryMock


class TestGetAllStudentsController(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_students_controller(self):
        request = self.factory.get('/get_all_students')
        repo = UserRepositoryMock()
        controller = GetAllStudentsController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "All students were successfully retrieved"
        assert len(response.body) == 5
