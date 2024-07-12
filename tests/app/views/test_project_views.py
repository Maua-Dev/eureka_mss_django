from django.test import TransactionTestCase
from app.models.project import Project
from app.models.user import User


class TestProjectView(TransactionTestCase):
    def setUp(self):
        User.objects.create(user_id=1, name='VITOR GUIRAO SOLLER', email='21.01444-2@maua.br', role='STUDENT')
        User.objects.create(user_id=2, name='JOAO VITOR CHOUERI BRANCO', email='21.01075-7@maua.br', role='STUDENT')
        User.objects.create(user_id=3, name='BRUNO VILARDI BUENO', email='19.00331-5@maua.br', role='STUDENT')
        User.objects.create(user_id=4, name='CARLOS EDUARDO DANTAS DE MENEZES', email='carlos.menezes@maua.br', role='ADVISOR')
        User.objects.create(user_id=5, name='ANA PAULA GONCALVES SERRA', email='ana.serra@maua.br', role='RESPONSIBLE')
        project = Project.objects.create(title="Teste", qualification="Engenharia da Computação", code="ECOM000", shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project.advisors.add(4)
        project.responsibles.add(5)
        project.students.add(1, 2, 3)
        project.save()

    def tearDown(self):
        Project.objects.all().delete()
        User.objects.all().delete()

    def test_create_project_view(self):
        response = self.client.post('/create_project', {
                "user_id": 10,
                "title": "Analisando a viabilidade de um sistema de monitoramento de idosos",
                "qualification": "Engenharia de Software",
                "code": "ES-01",
                "shift": "DIURNO",
                "stand_number": "1",
                "is_entrepreneurship": False,
                "responsibles": [5],
                "advisors": [4],
            },
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_update_project_view(self):
        response = self.client.put('/update_project', {
                "user_id": 10,
                "project_id": 1,
                "qualification": "LP 2",
            },
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_get_project_view(self):
        response = self.client.get('/get_project?project_id=1',
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_get_projects_by_role_view(self):
        response = self.client.get('/get_projects_by_role?user_id=1',
            content_type='application/json'
        )
        assert response.status_code == 200