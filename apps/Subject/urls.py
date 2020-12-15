from django.contrib import admin
from django.urls import path, include

from .views import subject_view


urlpatterns = [
    path('', subject_view, name='students_subjects'),
    ]