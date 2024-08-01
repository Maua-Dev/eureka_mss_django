import datetime

from django.test import TransactionTestCase

from app.models import User
from app.repos.user.user_repository_postgres import UserRepositoryPostgres


class TestUserRepositoryPostgres(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        User.objects.create(user_id=0, name="Vitor Soller", role="STUDENT")
        User.objects.create(user_id=1, name="Brancas", role="STUDENT")
        User.objects.create(user_id=2, name="Hector Guerrini", role="PROFESSOR")
        User.objects.create(user_id=3, name="Bruno Vilas", role="PROFESSOR")
        User.objects.create(user_id=4, name="Luigi Televisão", role="STUDENT")

    def tearDown(self):
        User.objects.all().delete()

    def test_get_user(self):
        repo = UserRepositoryPostgres()
        user = repo.get_user(1)
        assert user["user_id"] == 1
        assert user["name"] == "Brancas"
        
    def test_get_user_not_found(self):
        repo = UserRepositoryPostgres()
        user = repo.get_user(100)
        assert user is None

    def test_get_all_students(self):
        repo = UserRepositoryPostgres()
        students = repo.get_all_students()
        assert len(students) == 3
        assert students[0]["user_id"] == 0
        assert students[1]["user_id"] == 1
        assert students[2]["user_id"] == 4
        
    def test_get_all_professors(self):
        repo = UserRepositoryPostgres()
        professors = repo.get_all_professors()
        assert len(professors) == 2
        assert professors[0]["user_id"] == 2
        assert professors[1]["user_id"] == 3
        
