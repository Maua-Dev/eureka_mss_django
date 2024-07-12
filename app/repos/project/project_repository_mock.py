from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryMock(IProjectRepository):

        def __init__(self):
            self.projects = [
                {
                    "project_id": 1,
                    'title': "Teste",
                    'qualification': "Engenharia da Computação",
                    'code': "ECOM000",
                    'shift': "DIRUNO",
                    'stand_number': "1",
                    'is_entrepreneurship': False,
                    'advisors': [4],
                    'responsibles': [5],
                    'students': [1, 2],
                },
                {
                    "project_id": 2,
                    'title': "Teste 2",
                    'qualification': "Design",
                    'code': "DSGN123",
                    'shift': "NOTURNO",
                    'stand_number': "2",
                    'is_entrepreneurship': False,
                    'advisors': [4, 8],
                    'responsibles': [7],
                    'students': [3],
                },
                {
                    "project_id": 3,
                    'title': "Teste 3",
                    'qualification': "Administração",
                    'code': "ADM123",
                    'shift': "DIURNO",
                    'stand_number': "1",
                    'is_entrepreneurship': False,
                    'advisors': [4, 8],
                    'responsibles': [5],
                    'students': [6],
                }
            ]

        def get_project(self, project_id: int):
            for project in self.projects:
                if project['project_id'] == project_id:
                    return project
            return None

        def create_project(self, project):
            project['is_entrepreneurship'] = project.get("is_entrepreneurship", False)
            project['students'] = project.get("students", [])
            project['advisors'] = project.get("advisors", [])
            project['responsibles'] = project.get("responsibles", [])
            project["project_id"] = len(self.projects) + 1
            
            self.projects.append(project)
            return project

        def update_project(self, project):
            for i in range(len(self.projects)):
                if self.projects[i]['project_id'] == project['project_id']:
                    for key in project:
                        self.projects[i][key] = project[key]

                    return self.projects[i]
            return None
    
        def get_projects_by_role(self, user_id: int):
            projects = []
            for project in self.projects:
                if user_id in project['advisors'] or user_id in project['students'] or user_id in project['responsibles']:
                    projects.append(project)
            return projects
            