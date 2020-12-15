from django.urls import path

from .views import students_tasks, students_task_detail, done, not_done

urlpatterns = [
    path('', students_tasks, name='students_tasks'),
    path('<int:pk>/', students_task_detail, name='student_task_detail'),
    path('<int:pk>/done', done, name='done'),
    path('<int:pk>/not_done', not_done, name='not_done'),
]
