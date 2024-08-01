from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import AdvisorNotFound, ObjectNotFound, ProfessorForbiddenAction, ResponsibleNotFound, RoleCannotBeAnotherRole, RoleForbiddenAction, StudentCannotBeAdvisor, StudentCannotBeResponsible, StudentForbiddenAction, StudentNotFound, UserAlreadyInProject, MissingParameters, UserNotFound, WrongTypeParameter
from app.helpers.http.http_codes import Created, Forbidden, InternalServerError, BadRequest, NotFound
from app.helpers.http.http_models import HttpRequestModel
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.user.user_repository_interface import IUserRepository


class CreateProjectController(IController):

    def __init__(self, project_repo: IProjectRepository, user_repo: IUserRepository):
        super().__init__(project_repo)
        self.project_repo = project_repo
        self.user_repo = user_repo

    def __call__(self, request: HttpRequestModel):
        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return Created(
                body=response_data,
                message="The project was created successfully"
            )
        except ObjectNotFound as err:
            return NotFound(message=err.message)
            
        except WrongTypeParameter as err:
            return BadRequest(message=err.message)

        except RoleForbiddenAction as err:
            return Forbidden(message=err.message)

        except UserAlreadyInProject as err:
            return Forbidden(message=err.message)

        except RoleCannotBeAnotherRole as err:
            return Forbidden(message=err.message)
        
        except MissingParameters as err:
            return BadRequest(message=err.message)
        

        except Exception as err:
            return InternalServerError(
                message=str(err)
            )

    def error_handling(self, request: HttpRequestModel):
        if request.method != "POST":
            raise MissingParameters('body', 'create_project')

        data = request.data
        if data.get('title') is None:
            raise MissingParameters('title', 'create_project')

        if data.get('qualification') is None:
            raise MissingParameters('qualification', 'create_project')

        if data.get('code') is None:
            raise MissingParameters('code', 'create_project')

        if data.get('shift') is None:
            raise MissingParameters('shift', 'create_project')

        if data.get('stand_number') is None:
            raise MissingParameters('stand_number', 'create_project')

        if data.get('is_entrepreneurship') is None:
            raise MissingParameters('is_entrepreneurship', 'create_project')

        if data.get('students') is not None:
            if not isinstance(data['students'], list):
                raise WrongTypeParameter('students')
            
        if data.get('advisors') is not None:
            if not isinstance(data['advisors'], list):
                raise WrongTypeParameter('advisors')
            
        if data.get('responsibles') is not None:
            if not isinstance(data['responsibles'], list):
                raise WrongTypeParameter('responsibles')
            
        if data.get('user_id') is None:
            raise MissingParameters('user_id', 'create_project')

    def business_logic(self, request: HttpRequestModel):
        user = self.user_repo.get_user(user_id=request.data['user_id'])
        if user is None:
            raise UserNotFound()
        
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
                
                student_projects = self.repo.get_projects_by_role(user_id=student_id)
                if student_projects != []:
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
        
        project_created = self.repo.create_project(
            {key: value for key, value in request.data.items() if key != 'user_id'}
        )
        if project_created.get('students') is None:
            project_created['students'] = []
            
        if project_created.get('advisors') is None:
            project_created['advisors'] = []
            
        if project_created.get('responsibles') is None:
            project_created['responsibles'] = []
        
        
        return project_created
