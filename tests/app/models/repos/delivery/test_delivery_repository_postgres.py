from django.test import TransactionTestCase

from app.models import Delivery, Task, Project, User
from app.repos.delivery.delivery_repository_postgres import DeliveryRepositoryPostgres


class Test_DeliveryRepositoryPostgres(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        Task.objects.create(task_id=1, title="Dados do Trabalho", delivery_date="2023-05-22", responsible="STUDENT")
        Task.objects.create(task_id=2, title="Dados do Trabalho", delivery_date="2023-09-14", responsible="RESPONSIBLE")

        User.objects.create(user_id=1, name='VITOR GUIRAO SOLLER', email='21.01444-2@maua.br', role='STUDENT')
        User.objects.create(user_id=2, name='JOAO VITOR CHOUERI BRANCO', email='21.01075-7@maua.br', role='STUDENT')
        User.objects.create(user_id=3, name='BRUNO VILARDI BUENO', email='19.00331-5@maua.br', role='STUDENT')
        User.objects.create(user_id=4, name='CARLOS EDUARDO DANTAS DE MENEZES', email='carlos.menezes@maua.br',
                            role='ADVISOR')
        User.objects.create(user_id=5, name='ANA PAULA GONCALVES SERRA', email='ana.serra@maua.br', role='RESPONSIBLE')

        project = Project.objects.create(title="Teste", qualification="Engenharia da Computação", code="ECOM000",
                                         shift="DIURNO", stand_number="1", is_entrepreneurship=False)
        project.advisors.add(4)
        project.responsibles.add(5)
        project.students.add(1, 2, 3)
        project.save()

        Delivery.objects.create(task_id=2, project_id=1, user_id=4, content={"content": "Algum conteúdo"})

    def tearDown(self):
        Delivery.objects.all().delete()
        Task.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()


    def test_create_delivery(self):
        repo = DeliveryRepositoryPostgres()
        delivery = {
            "task_id": 1,
            "project_id": 1,
            "user_id": 3,
            "content": {"content": "Algum conteúdo"},
        }
        project = {
            'project_id': 1,
            'title': 'Teste',
            'qualification': 'Engenharia da Computação',
            'code': 'ECOM000',
            'shift': 'DIURNO',
            'stand_number': '1',
            'is_entrepreneurship': False,
            'advisors': [
                {
                    'user_id': 4,
                    'name': 'CARLOS EDUARDO DANTAS DE MENEZES',
                    'email': 'carlos.menezes@maua.br',
                    'role': 'ADVISOR'
                }
            ],
            'responsibles': [
                {
                    'user_id': 5,
                    'name': 'ANA PAULA GONCALVES SERRA',
                    'email': 'ana.serra@maua.br',
                    'role': 'RESPONSIBLE'
                }
            ],
            'students': [
                {
                    'user_id': 1,
                    'name': 'VITOR GUIRAO SOLLER',
                    'email': '21.01444-2@maua.br',
                    'role': 'STUDENT'
                },
                {
                    'user_id': 2,
                    'name': 'JOAO VITOR CHOUERI BRANCO',
                    'email': '21.01075-7@maua.br',
                    'role': 'STUDENT'
                },
                {
                    'user_id': 3,
                    'name': 'BRUNO VILARDI BUENO',
                    'email': '19.00331-5@maua.br',
                    'role': 'STUDENT'
                }
            ]
        }

        task = {
            'task_id': 1,
            'title': 'Dados do Trabalho',
            'delivery_date': '2023-05-22',
            'responsible': 'STUDENT'
        }
       
        user = {
            'user_id': 3,
            'name': 'BRUNO VILARDI BUENO',
            'email': '19.00331-5@maua.br',
            'role': 'STUDENT'
        }
        delivery_expected = {
            'delivery_id': 2,
            'task': {
                'task_id': 1,
                'title': 'Dados do Trabalho',
                'delivery_date': '2023-05-22',
                'responsible': 'STUDENT'
            },
            'project': {
                'project_id': 1,
                'title': 'Teste',
                'qualification': 'Engenharia da Computação',
                'code': 'ECOM000',
                'shift': 'DIURNO',
                'stand_number': '1',
                'is_entrepreneurship': False,
                'professors': [
                    {
                        'user_id': 4,
                        'name': 'CARLOS EDUARDO DANTAS DE MENEZES',
                        'email': 'carlos.menezes@maua.br',
                        'role': 'ADVISOR'
                    },
                    {
                        'user_id': 5,
                        'name': 'ANA PAULA GONCALVES SERRA',
                        'email': 'ana.serra@maua.br',
                        'role': 'RESPONSIBLE'
                    }
                ],
                'students': [
                    {
                        'user_id': 1,
                        'name': 'VITOR GUIRAO SOLLER',
                        'email': '21.01444-2@maua.br',
                        'role': 'STUDENT'
                    },
                    {
                        'user_id': 2,
                        'name': 'JOAO VITOR CHOUERI BRANCO',
                        'email': '21.01075-7@maua.br',
                        'role': 'STUDENT'
                    },
                    {
                        'user_id': 3,
                        'name': 'BRUNO VILARDI BUENO',
                        'email': '19.00331-5@maua.br',
                        'role': 'STUDENT'
                    }
                ]
            },
            'user': {
                'user_id': 3,
                'name': 'BRUNO VILARDI BUENO',
                'email': '19.00331-5@maua.br',
                'role': 'STUDENT'
            },
            'content': {"content": "Algum conteúdo"}
        }
        len_before = Delivery.objects.count()

        delivery_created = repo.create_delivery(delivery=delivery, user=user, task=task, project=project)
        len_after = Delivery.objects.count()


        assert len_after == len_before + 1
        assert delivery_created['content'] == delivery_expected['content']

    def test_get_delivery(self):
        repo = DeliveryRepositoryPostgres()
        delivery_id = 1

        delivery = repo.get_delivery(delivery_id)

        assert delivery['delivery_id'] == delivery_id
        assert delivery['task']['task_id'] == 2
        assert delivery['project']['project_id'] == 1
        assert delivery['user']['user_id'] == 4
        assert delivery['content'] == {"content": "Algum conteúdo"}


    def test_get_deliveries(self):
        repo = DeliveryRepositoryPostgres()
        project_id = 1

        deliveries = repo.get_deliveries(project_id)

        assert len(deliveries) == 1
        assert deliveries[0]['delivery_id'] == 1
        assert deliveries[0]['task']['task_id'] == 2
        assert deliveries[0]['project']['project_id'] == 1
        assert deliveries[0]['user']['user_id'] == 4
        assert deliveries[0]['content'] == {"content": "Algum conteúdo"}
