from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject

from apps.Task.models import Task
from ..users.decorators import student_required


@login_required
@student_required
def subject_view(request):
    user_group = request.user.student.group
    subjects = Subject.objects.filter(group=user_group)
    marks = {}
    student_id = request.user.student.id
    tasks = Task.objects.filter(student_id=student_id)
    for sub in subjects:
        one_mark = 0
        for task in tasks:
            if task.subject == sub:
                one_mark += task.mark
            else:
                continue
        marks.update({sub.title: one_mark})
    print(marks)
    return render(request, 'subjects.html', {'subjects': marks})
