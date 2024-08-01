from django.test import TestCase
from app.repos.user.user_repository_mock import UserRepositoryMock


class TestUserRepositoryMock(TestCase):
    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user(1)
        assert user == repo.users[0]
        
    def test_get_user_not_found(self):
        repo = UserRepositoryMock()
        user = repo.get_user(100)
        assert user is None

    def test_get_all_students(self):
        repo = UserRepositoryMock()
        students = repo.get_all_students()
        assert len(students) == 5
        
    def test_get_all_professors(self):
        repo = UserRepositoryMock()
        professors = repo.get_all_professors()
        assert len(professors) == 4