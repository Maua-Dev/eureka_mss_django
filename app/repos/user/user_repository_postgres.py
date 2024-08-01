from app.models import User
from app.repos.user.user_repository_interface import IUserRepository


class UserRepositoryPostgres(IUserRepository):

    def __init__(self):
        pass

    def get_user(self, user_id: int):
        try:
            return User.objects.get(user_id=user_id).to_dict()
        except:
            return None
        
    def get_all_students(self):
        return [student.to_dict() for student in User.objects.filter(role="STUDENT")]
    
    def get_all_professors(self):
        return [professor.to_dict() for professor in User.objects.filter(role="PROFESSOR")]