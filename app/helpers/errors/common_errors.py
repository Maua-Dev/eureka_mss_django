from app.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, field: str, method: str):
        super().__init__(f'Field {field} is missing for method {method}')


class ObjectNotFound(BaseError):
    def __init__(self, model: str, genre: str = 'o'):
        super().__init__(f'{model} não encontrad{genre}')


class RequestNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Requisição', genre='a')


class ProjectNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Projeto')


class TaskNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Tarefa', genre='a')


class DeliveryNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Entrega', genre='a')

class UserNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Usuário', genre='o')
        
class StudentNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Estudante', genre='o')

class AdvisorNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Orientador', genre='o')
    
class ResponsibleNotFound(ObjectNotFound):
    def __init__(self):
        super().__init__(model='Responsável', genre='o')

class RoleForbiddenAction(BaseError):
    def __init__(self, role: str):
        super().__init__(f'{role} não tem permissão para realizar esta ação')

class RoleCannotBeAnotherRole(BaseError):
    def __init__(self, role: str, another_role: str):
        super().__init__(f"{role} não pode ser {another_role}")
        
class StudentCannotBeAdvisor(RoleCannotBeAnotherRole):
    def __init__(self):
        super().__init__(role='Estudante', another_role='Orientador')

class StudentCannotBeResponsible(RoleCannotBeAnotherRole):
    def __init__(self):
        super().__init__(role='Estudante', another_role='Responsável')

class AdvisorForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Orientador')
        
class ResponsibleForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Responsável')

class StudentForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Estudante')
        
class ProfessorForbiddenAction(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Professor')


class StudentNotInProject(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Estudante')


class TeacherNotInProject(RoleForbiddenAction):
    def __init__(self):
        super().__init__(role='Professor')

class WrongTypeParameter(BaseError):
    def __init__(self, field: str = ''):
        super().__init__(f'Tipo de parâmetro incorreto para {field}')
        
class UserAlreadyInProject(BaseError):
    def __init__(self, role: str):
        super().__init__(f'{role} já cadastrado em um projeto')
