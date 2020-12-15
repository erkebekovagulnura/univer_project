from django.urls import path, include

from .views import task_create_view, teacher_cabinet, verified, not_verified

urlpatterns = [
        path('', task_create_view, name='teacher_task_create'),
        path('tasks/', teacher_cabinet, name='teacher_tasks'),
        path('<int:pk>/verified', verified, name='verified'),
        path('<int:pk>/not_verified', not_verified, name='not_verified'),
]