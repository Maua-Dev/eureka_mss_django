from typing import Dict, List

from app.enums.task_responsible_enum import TASK_RESPONSIBLE
from app.repos.task.task_repository_interface import ITaskRepository


class TaskRepositoryMock(ITaskRepository):
    tasks: List[Dict[str, str]]

    def __init__(self):
        self.tasks = [
            {
                "task_id": 1,
                "title": "Dados do trabalho",
                "delivery_date": "2023-05-15",
                "responsible": TASK_RESPONSIBLE.STUDENT.value
            },
            {
                "task_id": 2,
                "title": "Dados do trabalho",
                "delivery_date": "2023-05-22",
                "responsible": TASK_RESPONSIBLE.ADVISOR.value
            },
            {
                "task_id": 3,
                "title": "Dados do trabalho",
                "delivery_date": "2023-09-14",
                "responsible": TASK_RESPONSIBLE.RESPONSIBLE.value
            },
            {
                "task_id": 4,
                "title": "Pôster Técnico (PDF)",
                "delivery_date": "2023-10-01",
                "responsible": TASK_RESPONSIBLE.STUDENT.value
            },
            {
                "task_id": 5,
                "title": "Pôster Técnico (PDF)",
                "delivery_date": "2023-10-03",
                "responsible": TASK_RESPONSIBLE.ADVISOR.value
            },
            {
                "task_id": 6,
                "title": "Pôster Imagem",
                "delivery_date": "2023-09-17",
                "responsible": TASK_RESPONSIBLE.STUDENT.value
            },
            {
                "task_id": 7,
                "title": "Pôster Imagem",
                "delivery_date": "2023-09-20",
                "responsible": TASK_RESPONSIBLE.ADVISOR.value
            },
            {
                "task_id": 8,
                "title": "Tirar usuário do sistema",
                "delivery_date": "2023-10-10",
                "responsible": TASK_RESPONSIBLE.ADMIN.value
            }
        ]

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task['task_id'] == task_id:
                return task
        return None 