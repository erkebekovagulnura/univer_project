from django.db import models


class Faculty(models.Model):
    title = models.CharField(max_length=50, verbose_name='Факультет', unique=True)

    def __str__(self):
        return f'{self.title}'


class Groups(models.Model):
    title = models.CharField(max_length=10, verbose_name="Группа", unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'
