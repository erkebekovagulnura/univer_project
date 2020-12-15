from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..Subject.models import Subject
from apps.Groups_faculties.models import Groups
from .models import Student, Teacher

from django.contrib.auth import get_user_model

User = get_user_model()


class StudentSignUpForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Groups.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'father_name', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.group = self.cleaned_data.get('group')
        student.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'father_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.subject = self.cleaned_data.get('subject')
        teacher.save()
        return user
