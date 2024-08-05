from django.db import models


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    content = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "delivery_id": self.delivery_id,
            "task": self.task.to_dict() if self.task != dict else self.task,
            "project": self.project.to_dict() if self.project != dict else self.project,
            "user": self.user.to_dict() if self.user != dict else self.user,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "content": self.content,
        }
