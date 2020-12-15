from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView, TemplateView,
    DetailView, ListView)

from apps.Task.models import Task
from apps.users.decorators import student_required
from apps.users.forms import StudentSignUpForm, TeacherSignUpForm

User = get_user_model()


class IndexPageView(TemplateView):
    template_name = 'index.html'


class NewUserSignUpView(TemplateView):
    template_name = 'registration/signup.html'


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student aka'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'училка'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


@method_decorator([login_required, student_required], name='dispatch')
class StudentsCabinet(TemplateView):
    template_name = 'cabinet/student.html'



