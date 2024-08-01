from typing import Dict, List

from app.enums.task_responsible_enum import TASK_RESPONSIBLE
from app.repos.user.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: List[Dict[str, str]]

    def __init__(self):
        self.users = [
            {
                "user_id": 1,
                "name": "VITOR GUIRAO SOLLER",
                "email": "21.01444-2@maua.br",
                "role": "STUDENT"
            },
            {
                "user_id": 2,
                "name": "JOAO VITOR CHOUERI BRANCO",
                "email": "21.01075-7@maua.br",
                "role": "STUDENT"
            },
            {
                "user_id": 3,
                "name": "BRUNO VILARDI BUENO",
                "email": "19.00331-5@maua.br",
                "role": "STUDENT"
            },
            {
                "user_id": 4,
                "name": "CARLOS EDUARDO DANTAS DE MENEZES",
                "email": "carlos.menezes@maua.br",
                "role": "PROFESSOR" # advisor
            },
            {
                "user_id": 5,
                "name": "ANA PAULA GONCALVES SERRA",
                "email": "ana.serra@maua.br",
                "role": "PROFESSOR" # responsible
            },
            {
                "user_id": 6,
                "name": "SILVIO SANTOS",
                "email": "silvio.santos@sbt.br",
                "role": "STUDENT"
            },
            {
                "user_id": 7,
                "name": "JOSE MARIA",
                "email": "jose.maria@sbt.br",
                "role": "PROFESSOR" # responsible	
            },
            {
                "user_id": 8,
                "name": "VANDERLEI CUNHA PARRO",
                "email": "vcp@maua.br",
                "role": "PROFESSOR" # advisor
            },
            {
                "user_id": 9,
                "name": "RODRIGO MORALES MILES",
                "email": "rodrigo.miles@maua.br",
                "role": "STUDENT" # student without project
            },
            {
                "user_id": 10,
                "name": "FERNANDO ANDRADE RODRIGUES",
                "email": "fernando.rodrigues@maua.br",
                "role": "ADMIN"
            }
            
        ]

    def get_user(self, user_id: int):
        for user in self.users:
            if user['user_id'] == user_id:
                return user
        return None
    
    def get_all_students(self):
        return [student for student in self.users if student["role"] == "STUDENT"]
    
    def get_all_professors(self):
        return [professor for professor in self.users if professor["role"] == "PROFESSOR"]