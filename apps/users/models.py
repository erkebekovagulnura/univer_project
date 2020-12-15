from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.Groups_faculties.models import Groups
from apps.Subject.models import Subject


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    father_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Студент {self.user.last_name} {self.user.first_name} {self.user.father_name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.father_name}'
