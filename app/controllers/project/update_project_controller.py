from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import AdvisorForbiddenAction, AdvisorNotFound, MissingParameters, ObjectNotFound, ProfessorForbiddenAction, ResponsibleForbiddenAction, ResponsibleNotFound, RoleCannotBeAnotherRole, RoleForbiddenAction, StudentCannotBeAdvisor, StudentCannotBeResponsible, StudentForbiddenAction, StudentNotFound, UserAlreadyInProject, UserNotFound
from app.helpers.http.http_codes import Forbidden, InternalServerError, BadRequest, OK, NotFound
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.user.user_repository_interface import IUserRepository


class UpdateProjectController(IController):
    def __init__(self, project_repo: IProjectRepository, user_repo: IUserRepository):
        super().__init__(project_repo=project_repo, user_repo=user_repo)
        self.project_repo = project_repo
        self.user_repo = user_repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)
            
            if response_data is None:
                return NotFound(
                    message="Projeto não encontrado"
                ) 

            return OK(
                body=response_data,
                message="The project was updated successfully"
            )

        except MissingParameters as err:
            return BadRequest(message=err.message)
        
        except ObjectNotFound as err:
            return NotFound(message=err.message)

        except RoleForbiddenAction as err:
            return Forbidden(message=err.message)

        except UserAlreadyInProject as err:
            return Forbidden(message=err.message)

        except RoleCannotBeAnotherRole as err:
            return Forbidden(message=err.message)

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "PUT":
            raise MissingParameters('body', 'update_project')

        data = request.data

        if data.get('project_id') is None:
            raise MissingParameters('project_id', 'update_project')
        
        if data.get('user_id') is None:
            raise MissingParameters('user_id', 'update_project')

    def business_logic(self, request: HttpRequestModel):
        user_id = request.data['user_id']
        user = self.user_repo.get_user(user_id=user_id)
        if user is None:
            raise UserNotFound()
        
        if request.data.get('students') is not None or request.data.get('advisors') is not None or request.data.get('responsibles') is not None:
            if user['role'] != 'ADMIN':
                if user['role'] == 'STUDENT':
                    raise StudentForbiddenAction()
                elif user['role'] == 'PROFESSOR':
                    raise ProfessorForbiddenAction()
                    
            
        if request.data.get('students') is not None:
            for student_id in request.data['students']:
                student = self.user_repo.get_user(user_id=student_id)
                if student is None:
                    raise StudentNotFound()

                student_projects = self.project_repo.get_projects_by_role(user_id=student_id)
                if student_projects != [] and not student_projects[0]['project_id'] == request.data['project_id']:
                    raise UserAlreadyInProject(role="Estudante")
        
        if request.data.get('advisors') is not None:
            for advisor_id in request.data['advisors']:
                advisor = self.user_repo.get_user(user_id=advisor_id)
                if advisor is None:
                    raise AdvisorNotFound()
                if advisor['role'] == 'STUDENT':
                    raise StudentCannotBeAdvisor()
                
        if request.data.get('responsibles') is not None:
            for responsible_id in request.data['responsibles']:
                responsible = self.user_repo.get_user(user_id=responsible_id)
                if responsible is None:
                    raise ResponsibleNotFound()
                if responsible['role'] == 'STUDENT':
                    raise StudentCannotBeResponsible()
        
        return self.project_repo.update_project(request.data)
