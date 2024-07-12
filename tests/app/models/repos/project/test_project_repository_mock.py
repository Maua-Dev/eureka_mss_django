from django.test import TestCase

from app.repos.project.project_repository_mock import ProjectRepositoryMock


class TestProjectRepositoryMock(TestCase):

    def test_create_project(self):
        repo = ProjectRepositoryMock()
        project = {
            "project_id": 2,
            'title': "Teste",
            'qualification': "Engenharia da Computação",
            'code': "ECOM000",
            'shift': "DIRUNO",
            'stand_number': "1",
            'is_entrepreneurship': False,
            'advisors': [4],
            'responsibles': [7],
            'students': [4, 5],
        }

        len_before = len(repo.projects)

        repo.create_project(project)

        assert len(repo.projects) == len_before + 1

    def test_update_project(self):

        repo = ProjectRepositoryMock()

        project = {
            "project_id": 1,
            'title': "Teste2",
        }

        repo.update_project(project)

        assert repo.projects[0]['title'] == 'Teste2'

    def test_get_project(self):
        repo = ProjectRepositoryMock()
        project = repo.get_project(1)
        assert project == repo.projects[0]

    def test_get_projects_by_role(self):
        repo = ProjectRepositoryMock()
        projects1 = repo.get_projects_by_role(user_id=1)
        assert projects1 == [repo.projects[0]]
        
        projects2 = repo.get_projects_by_role(user_id=4)
        assert projects2 == repo.projects
        
        projects3 = repo.get_projects_by_role(user_id=5)
        assert projects3 == [repo.projects[0], repo.projects[2]]
        
        projects4 = repo.get_projects_by_role(user_id=100)
        assert projects4 == []
        
        projects5 = repo.get_projects_by_role(user_id=7)
        assert projects5 == [repo.projects[1]] 
        
        