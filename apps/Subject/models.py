from django.db import models
from apps.Groups_faculties.models import *


class Subject(models.Model):
    title = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    group = models.ManyToManyField(Groups, related_name='groups_subject')

    def __str__(self):
        return f'{self.title}'