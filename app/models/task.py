from django.db import models


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    delivery_date = models.DateField()
    responsible = models.CharField(max_length=255)  # Student, Professor, Responsible

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "delivery_date": self.delivery_date.strftime("%Y-%m-%d"),
            "responsible": self.responsible
        }
