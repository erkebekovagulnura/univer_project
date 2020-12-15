from django import forms

from apps.Shcedule.models import Shcedule


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Shcedule
        fields = '__all__'
