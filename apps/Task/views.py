from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.Task.forms import TaskCreateForm, TaskStudentFilter

from apps.users.models import Student

from .models import Task
from apps.Subject.models import Subject
from ..users.decorators import student_required


@login_required
@student_required
def students_tasks(request):
    student = request.user.student
    tasks = Task.objects.filter(student=student)
    form = TaskStudentFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['search']:
            try:
                subject = Subject.objects.get(title__icontains=form.cleaned_data['search'])
                tasks = Task.objects.filter(subject=subject.id, student=student)
            except Subject.DoesNotExist:
                tasks = None
                return render(request, 'tasks.html', {'tasks': tasks, 'form': form})

        if form.cleaned_data['done'] and form.cleaned_data['not_done']:
            return render(request, 'tasks.html', {'tasks': tasks, 'form': form})
        elif form.cleaned_data['done']:
            tasks = Task.objects.filter(student=student, done=True)
            return render(request, 'tasks.html', {'tasks': tasks, 'form': form})
        elif form.cleaned_data['not_done']:
            tasks = Task.objects.filter(student=student, done=False)
            return render(request, 'tasks.html', {'tasks': tasks, 'form': form})
    return render(request, 'tasks.html', {'tasks': tasks, 'form': form})


@login_required
@student_required
def students_task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks_detail.html', {'task': task})


@login_required
@student_required
def done(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()
    return redirect('students_tasks')


@login_required
@student_required
def not_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = False
    task.save()
    return redirect('students_tasks')
