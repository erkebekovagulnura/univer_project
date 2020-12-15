from django.urls import path

from .views import ScheduleView, CreateSchedule

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('create/', CreateSchedule.as_view(), name='create_schedule'),

    ]