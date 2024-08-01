from abc import abstractmethod

from app.repos.repo_interface import RepoInterface


class IUserRepository(RepoInterface):

    @abstractmethod
    def get_user(self):
        """
        Return user by user_id.
        """
        pass
    
    @abstractmethod
    def get_all_students(self):
        """
        Return all students.
        """
        pass
    
    @abstractmethod
    def get_all_professors(self):
        """
        Return all professors.
        """
        pass
