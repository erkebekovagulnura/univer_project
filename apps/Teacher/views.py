from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.Task.forms import TaskCreateForm
from apps.Task.models import Task
from apps.Teacher.forms import TeacherTaskFilter
from apps.users.decorators import teacher_required
from apps.users.models import Student


@login_required
@teacher_required
def task_create_view(request):
    user = request.user
    form = TaskCreateForm()
    if request.method == 'POST':
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            students_group = clean_data.get('group')
            students = Student.objects.filter(group=students_group)
            for student in students:
                new_task = Task.create(
                    title=clean_data['title'],
                    description=clean_data['description'],
                    email=request.user.email,
                    teacher=request.user,
                    student=student,
                    subject=request.user.teacher.subject
                )
        return redirect('teacher_task_create')
    return render(request, 'teachers_cabinet/teacher.html', locals())


@login_required
@teacher_required
def teacher_cabinet(request):
    teacher = request.user
    tasks = Task.objects.filter(teacher=teacher)
    form = TeacherTaskFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['verified'] and form.cleaned_data['not_verified']:
            return render(request, 'teachers_cabinet/tasks.html', {'tasks': tasks, 'form': form})
        elif form.cleaned_data['verified']:
            tasks = Task.objects.filter(teacher=teacher, verified=True)
            return render(request, 'teachers_cabinet/tasks.html', {'tasks': tasks, 'form': form})
        elif form.cleaned_data['not_verified']:
            tasks = Task.objects.filter(teacher=teacher, verified=False)
            return render(request, 'teachers_cabinet/tasks.html', {'tasks': tasks, 'form': form})
    return render(request, 'teachers_cabinet/tasks.html', {'tasks': tasks, 'form': form})


@login_required
@teacher_required
def verified(request, pk):
    task = Task.objects.get(pk=pk)
    task.verified = True
    task.mark = 15
    task.save()
    return redirect('teacher_tasks')


@login_required
@teacher_required
def not_verified(request, pk):
    task = Task.objects.get(pk=pk)
    task.verified = False
    task.mark = 0
    task.save()
    return redirect('teacher_tasks')
