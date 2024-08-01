import json

from app.controllers.controller_interface import IController
from app.helpers.errors.common_errors import AdvisorForbiddenAction, ObjectNotFound, MissingParameters, ProjectNotFound, RequestNotFound, ResponsibleForbiddenAction, RoleForbiddenAction, StudentForbiddenAction, StudentNotInProject, TaskNotFound, TeacherNotInProject, UserNotFound
from app.helpers.http.http_codes import Created, BadRequest, InternalServerError, NotFound, Forbidden
from app.helpers.http.http_models import HttpRequestModel
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository
from app.repos.project.project_repository_interface import IProjectRepository
from app.repos.task.task_repository_interface import ITaskRepository
from app.repos.user.user_repository_interface import IUserRepository


class CreateDeliveryController(IController):

    def __init__(self, delivery_repo: IDeliveryRepository, task_repo: ITaskRepository, project_repo: IProjectRepository, user_repo: IUserRepository): 
        super().__init__(delivery_repo=delivery_repo, task_repo=task_repo, project_repo=project_repo, user_repo=user_repo)

    def __call__(self, request: HttpRequestModel):

        try:
            self.error_handling(request)
            response_data = self.business_logic(request)

            return Created(
                body=response_data,
                message="The delivery was created successfully"
            )

        except MissingParameters as e:
            return BadRequest(
                message=str(e)
            )

        except ObjectNotFound as e:
            return NotFound(
                message=str(e)
            )

        except RoleForbiddenAction as e:
            return Forbidden(
                message=str(e)
            )

        except Exception as e:
            return InternalServerError(
                message=str(e)
            )

    def error_handling(self, request: HttpRequestModel):
        try:
            if request.method != "POST":
                raise Exception()
        except:
            raise RequestNotFound()
        
        
        if request.data.get('task_id') is None:
            raise MissingParameters('task_id', 'create_delivery')

        if request.data.get('project_id') is None:
            raise MissingParameters('project_id', 'create_delivery')

        if request.data.get('user_id') is None:
            raise MissingParameters('user_id', 'create_delivery')

        if request.data.get('content') is None:
            raise MissingParameters('content', 'create_delivery')


    def business_logic(self, request: HttpRequestModel):
        delivery = request.data
        
        try:
            task = self.task_repo.get_task(delivery['task_id'])
            if task is None:
                raise Exception()
        except:
            raise TaskNotFound()
        try:
            project = self.project_repo.get_project(delivery['project_id'])
            if project is None:
                raise Exception()
        except:
            raise ProjectNotFound()
        try:
            user = self.user_repo.get_user(delivery['user_id'])
            if user is None:
                raise Exception()
        except:
            raise UserNotFound()
        
        user_role = user['role']
        if user_role == "PROFESSOR":
            advisors_id = project['advisors']
            responsibles_id = project['responsibles']
            if user['user_id'] not in advisors_id and user['user_id'] not in responsibles_id:
                raise TeacherNotInProject()

            if user['user_id'] in advisors_id:
                user_role = "ADVISOR"
            
            if user['user_id'] in responsibles_id:
                user_role = "RESPONSIBLE"
        
        if user_role == "STUDENT":
            students_id = project['students']
            if user['user_id'] not in students_id:
                raise StudentNotInProject()
        
        if user_role == 'STUDENT' and task['responsible'] in ['ADVISOR', 'RESPONSIBLE', 'ADMIN']:
            raise StudentForbiddenAction()
    
        if user_role == 'ADVISOR' and task['responsible'] in ['RESPONSIBLE', 'ADMIN']:
            raise AdvisorForbiddenAction()
        
        if user_role == 'RESPONSIBLE' and task['responsible'] == 'ADMIN':
            raise ResponsibleForbiddenAction()
        
        response = self.delivery_repo.create_delivery(
            delivery=delivery, 
            user=user, 
            task=task, 
            project=project
        )

        return response
