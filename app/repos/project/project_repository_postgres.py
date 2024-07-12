from app.models import Project, User
from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryPostgres(IProjectRepository):

        def __init__(self):
            pass
        
        def get_project(self, project_id: int):
            try:
                return Project.objects.get(project_id=project_id).to_dict()
            except:
                return None
            
        def get_projects_by_role(self, user_id: int):
            student_projects = []
            try:
                student_projects = Project.objects.filter(students__user_id=user_id)
            except: pass
            if len(student_projects) > 0:
                return [project.to_dict() for project in student_projects]    

            advisors_project = []
            try:
                advisors_project = Project.objects.filter(advisors__user_id=user_id)
            except: pass
            if len(advisors_project) > 0:
                return [project.to_dict() for project in advisors_project]
            
            responsibles_project = []
            try:
                responsibles_project = Project.objects.filter(responsibles__user_id=user_id)
            except: pass
            if len(responsibles_project) > 0:
                return [project.to_dict() for project in responsibles_project]
            
            return []
                


        def update_project(self, project):
            project_to_update = Project.objects.get(project_id=project['project_id'])

            to_update = project


            if 'responsibles' in project:
                responsibles = User.objects.filter(user_id__in=project['responsibles'])
                project_to_update.responsibles.set(responsibles)
                to_update.pop('responsibles')
                
            if 'advisors' in project:
                advisors = User.objects.filter(user_id__in=project['advisors'])
                project_to_update.professors.set(advisors)
                to_update.pop('advisors')

            if 'students' in project:
                students = User.objects.filter(user_id__in=project['students'])
                project_to_update.students.set(students)
                to_update.pop('students')

            for key, value in to_update.items():
                setattr(project_to_update, key, value)

            project_to_update.save()

            return project_to_update.to_dict()

        def create_project(self, project):
            project_created = Project.objects.create(
                title=project['title'],
                qualification=project['qualification'],
                code=project['code'],
                shift=project['shift'],
                stand_number=project['stand_number'],
                is_entrepreneurship=project['is_entrepreneurship']
            )

            if len(project.get('advisors', [])) + len(project.get('responsibles', [])) + len(project.get('students', [])) > 0:
                if 'advisors' in project:
                    advisors = User.objects.filter(user_id__in=project['advisors'])
                    project_created.advisors.set(advisors)
                    
                if 'responsibles' in project:
                    responsibles = User.objects.filter(user_id__in=project['responsibles'])
                    project_created.responsibles.set(responsibles)

                if 'students' in project:
                    students = User.objects.filter(user_id__in=project['students'])
                    project_created.students.set(students)

                project_created.save()  
                
            return project_created.to_dict()
