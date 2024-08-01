from django.test import TestCase, RequestFactory
from app.controllers.user.get_all_professors_controller import GetAllProfessorsController

from app.repos.user.user_repository_mock import UserRepositoryMock


class TestGetAllProfessorsController(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_professors_controller(self):
        request = self.factory.get('/get_all_professors')
        repo = UserRepositoryMock()
        controller = GetAllProfessorsController(repo)
        response = controller(request)

        assert response.status_code == 200
        assert response.message == "All professors were successfully retrieved"
        assert len(response.body) == 4
