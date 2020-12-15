from django import forms

from apps.Groups_faculties.models import Groups
from .models import Task


class TaskCreateForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Groups.objects.all()
    )

    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')


class TaskStudentFilter(forms.Form):
    search = forms.CharField(max_length=50, label="Поиск по предмету", required=False, strip=True)
    done = forms.BooleanField(label="выполненные", required=False, widget=forms.CheckboxInput)
    not_done = forms.BooleanField(label="не выполненные", required=False, widget=forms.CheckboxInput)
