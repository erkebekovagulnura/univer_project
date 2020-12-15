from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import Student

from apps.Subject.models import Subject

User = get_user_model()


class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    deadline = models.DateField(null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students_task', null=True)
    done = models.BooleanField(default=False)
    mark = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def create(cls, subject, title, description, email, teacher, student, deadline=None):
        task = cls(
            subject=subject,
            title=title,
            description=description,
            email=email,
            deadline=deadline,
            teacher=teacher,
            student=student,
        )
        return task.save()
