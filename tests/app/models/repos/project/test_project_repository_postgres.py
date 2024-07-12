from django.test import TransactionTestCase

from app.models import User, Project
from app.repos.project.project_repository_postgres import ProjectRepositoryPostgres


class TestProjectRepositoryPostgres(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        User.objects.create(user_id=1, name='VITOR GUIRAO SOLLER', email='21.01444-2@maua.br', role='STUDENT')
        User.objects.create(user_id=2, name='JOAO VITOR CHOUERI BRANCO', email='21.01075-7@maua.br', role='STUDENT')
        User.objects.create(user_id=3, name='BRUNO VILARDI BUENO', email='19.00331-5@maua.br', role='STUDENT')
        User.objects.create(user_id=4, name='CARLOS EDUARDO DANTAS DE MENEZES', email='carlos.menezes@maua.br', role='ADVISOR')
        User.objects.create(user_id=5, name='ANA PAULA GONCALVES SERRA', email='ana.serra@maua.br', role='RESPONSIBLE')
        User.objects.create(user_id=6, name='PAULO SIQUEIRA', email='paulo.siqueira@maua.br', role='STUDENT')
        project = Project.objects.create(title="Teste", qualification="Engenharia da Computação", code="ECOM000", shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project.advisors.add(4)
        project.responsibles.add(5)
        project.students.add(1)
        project.save()
        
        project2 = Project.objects.create(title="Teste2", qualification="Engenharia da Computação", code="ECOM001", shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project2.advisors.add(4)
        project2.responsibles.add(5)
        project2.students.add(2)
        project2.save()
        
        project3 = Project.objects.create(title="Teste3", qualification="Engenharia da Computação", code="ECOM002", shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project3.advisors.add(4)
        project3.students.add(3)
        project3.save()
        
        

    def tearDown(self):
        Project.objects.all().delete()
        User.objects.all().delete()

    def test_update_project(self):
        repo = ProjectRepositoryPostgres()

        project = {
            "project_id": 1,
            'title': "Teste2",
            'is_entrepreneurship': True,
        }

        repo.update_project(project)

        assert Project.objects.get(project_id=1).title == 'Teste2'
        assert Project.objects.get(project_id=1).is_entrepreneurship

    def test_update_project_members(self):
        repo = ProjectRepositoryPostgres()

        project = {
            "project_id": 2,
            'title': "Teste2",
            'students': [1, 2],
            'responsibles': [5],
        }

        repo.update_project(project)

        assert Project.objects.get(project_id=2).students.count() == 2
        assert Project.objects.get(project_id=2).title == 'Teste2'
        assert Project.objects.get(project_id=2).responsibles.count() == 1

    def test_get_project(self):
        repo = ProjectRepositoryPostgres()

        project = repo.get_project(1)

        assert project['title'] == 'Teste'
        assert project['is_entrepreneurship'] == False
        
    def test_get_project_not_found(self):
        repo = ProjectRepositoryPostgres()

        project = repo.get_project(99)

        assert project is None    
    
    def test_create_project(self):
        repo = ProjectRepositoryPostgres()
        project = {
            'title': "Estudo da Computação Quântica",
            'qualification': "Engenharia da Computação",
            'code': "ECOM000",
            'shift': "DIURNO",
            'stand_number': "1",
            'is_entrepreneurship': False,
            'students': [1, 2, 3],
            'advisors': [4],
            'responsibles': [5]
        }

        count = Project.objects.count()

        repo.create_project(project)

        assert Project.objects.count() == count + 1

    def test_get_projects_by_role(self):
        repo = ProjectRepositoryPostgres()
        projects1 = repo.get_projects_by_role(user_id=1)
        assert len(projects1) == 1
        assert type(projects1) == list
        assert type(projects1[0]) == dict
        
        projects2 = repo.get_projects_by_role(user_id=2)
        assert len(projects2) == 1
        assert type(projects2) == list
        assert type(projects2[0]) == dict

        projects3 = repo.get_projects_by_role(user_id=3)
        assert len(projects3) == 1
        assert type(projects3) == list
        assert type(projects3[0]) == dict

        projects4 = repo.get_projects_by_role(user_id=4)
        assert len(projects4) == 3
        assert type(projects4) == list
        assert type(projects4[0]) == dict

        projects5 = repo.get_projects_by_role(user_id=5)
        assert len(projects5) == 2
        assert type(projects5) == list
        assert type(projects5[0]) == dict

        projects6 = repo.get_projects_by_role(user_id=6)
        assert len(projects6) == 0
        assert type(projects6) == list
