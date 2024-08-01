from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    advisors = models.ManyToManyField('User', related_name='advisors', blank=True)
    responsibles = models.ManyToManyField('User', related_name='responsibles', blank=True)
    stand_number = models.CharField(max_length=255)
    is_entrepreneurship = models.BooleanField(default=False)
    students = models.ManyToManyField('User', related_name='students', blank=True)

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.title,
            "qualification": self.qualification,
            "code": self.code,
            "shift": self.shift,
            "stand_number": self.stand_number,
            "is_entrepreneurship": self.is_entrepreneurship,
            "advisors": [advisor.to_dict() for advisor in self.advisors.all()] if self.advisors != list else [],
            "responsibles": [responsible.to_dict() for responsible in self.responsibles.all()] if self.responsibles != list else [],
            "students": [student.to_dict() for student in self.students.all()] if self.students != list else []
        }
