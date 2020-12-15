from django.contrib import admin
from django.urls import path, include

from .views import StudentSignUpView, TeacherSignUpView, NewUserSignUpView, IndexPageView, StudentsCabinet

urlpatterns = [
    path('', IndexPageView.as_view()),
    path('accounts/registration/', NewUserSignUpView.as_view(), name='new_register'),
    path('accounts/registration/student/', StudentSignUpView.as_view(), name='student_register'),
    path('accounts/registration/teacher/', TeacherSignUpView.as_view(), name='teacher_register'),
    path('student/', StudentsCabinet.as_view(), name='student_cabinet'),
    path('teacher/', include('apps.Teacher.urls')),
]
